from django.views import View

from django.shortcuts import render, redirect

import importlib

from django.urls import resolve

from django.contrib import messages

import re


class RelatedFormView:

    form = None
    parent = None
    parent_field_name = None
    formalias = None
    form_instance = None
    parent_pk = None

    def __init__(self, **kwargs):

        self.model = self.form().instance.__class__

    def fetch(self, parent_instance=None, data=None, files=None):
        if not getattr(self, 'parent_field_name', None):
            self.parent_field_name = self.parent.class_name.lower() 
        dataset = self.model.objects.filter(**{self.parent_field_name: parent_instance}) if parent_instance else None
        last_record = dataset.latest('id') if dataset else None
        self.form_instance = self.form(data=data, files=files, instance=last_record, initial={self.parent_field_name: parent_instance})
        return self.form_instance

    def set_parent(self, parent):
        self.parent = parent


class MainView(View):

    '''
    Conceito: Abstração para views com padronização de parâmetros e hierarquia de views

    '''
    children = []
    related = []
    url_triggers = []
    parent = None
    saved_model = None
    formalias = None
    setalias = None
    pkalias = None
    parent_field_name = None

    def __init__(self, **kwargs):
        self.model = self.form().instance.__class__
        self.class_name = self.model.__name__
        self.bind_children = self.get_children()
        self.bind_related = self.get_related()
        if not getattr(self, 'pkalias', None):
            self.pkalias = 'pk{}'.format(self.class_name.lower())
        if not getattr(self, 'formalias', None):
            self.formalias = "form{}".format(self.class_name.lower())
        if not getattr(self, 'setalias', None):
            self.setalias = "set{}".format(self.class_name.lower())

        super().__init__(**kwargs)

    #Parte deste código deste dispatch foi copiado do código original do Django. Adapatado para comportar hierarquia entre views
    def dispatch(self, request, *args, **kwargs):

        child_target = self.get_target_child(request, *args, **kwargs)
        
        if child_target:
            return child_target.dispatch(request, *args, **kwargs)

        pkdelete = kwargs.get('pkdelete', None)
        if pkdelete:
            return self.delete(request=request, *args, **kwargs)

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:        
            handler = self.http_method_not_allowed

        return handler(request, *args, **kwargs)

    def fetch_template_keys(self, request, *args, **kwargs):

        pk = kwargs.get(self.pkalias, None)

        if pk and self.parent_field_name:
            parent_pk = (getattr(self.model.objects.get(pk=pk), self.parent_field_name)).pk
        else:
            parent_pk = kwargs.get(self.parent.pkalias, None) if self.parent else None

        parent_reference = {self.parent_field_name: parent_pk} if self.parent_field_name and parent_pk else None
        model_instance = self.model.objects.get(pk=pk) if pk else None          

        passed_form_error = kwargs.get(self.formalias, None)

        form = passed_form_error if passed_form_error else self.form(initial=parent_reference, instance=model_instance)

        model_set = self.model.objects.filter(**parent_reference) if parent_reference else self.model.objects.all()

        children_tuple_template_keys = []

        for child in self.bind_children:
            set_child = child.model.objects.filter(**{child.parent_field_name: model_instance}) if model_instance else []
            form_child_initial = {child.parent_field_name: model_instance} if model_instance else None
            children_tuple_template_keys.append( (child.formalias, child.form(initial=form_child_initial), ) )
            children_tuple_template_keys.append( (child.setalias, set_child, ) )

        related_tuple_template_keys = []

        for related in self.bind_related:
            related_passed_form_error = kwargs.get(related.formalias, None)

            form_related = related_passed_form_error if related_passed_form_error else related.fetch(parent_instance=model_instance)

            related_tuple_template_keys.append( (related.formalias, form_related, ) )

        parent_template_keys = self.parent.fetch_template_keys(request, *args, **{**kwargs, **{self.parent.pkalias: parent_pk}}) if self.parent else {}

        return {
            **parent_template_keys,
            **(dict(children_tuple_template_keys)),
            **(dict(related_tuple_template_keys)),
            self.formalias: form,
            self.setalias: model_set,
            self.pkalias: pk,
            **self.template_keys(request, *args, **kwargs)
        }

    def template_keys(self, request, *args, **kwargs):
        return {}

    def get(self, request, *args, **kwargs):

        #print(self.fetch_template_keys(request, *args, **kwargs))

        return render(request, self.template_name, {
            **self.fetch_template_keys(request, *args, **kwargs)
        })

    def post(self, request, *args, **kwargs):

        pk = kwargs.get(self.pkalias, None)
        model_instance = self.model.objects.get(pk=pk) if pk else None 

        form = self.form(request.POST, request.FILES, instance=model_instance)

        tuple_forms_list = []

        related_error = False
        for related in self.bind_related:
            related.fetch(parent_instance=model_instance, data=request.POST, files=request.FILES)
            related.form_instance.fields[related.parent_field_name].required = False
            if not related.form_instance.is_valid():
                related_error = True
            tuple_forms_list.append( (related.formalias, related.form_instance, ) )

        if not related_error and form.is_valid():
            self.saved_model = form.save()
            messages.success(request, "Objeto {} {} com sucesso".format(self.saved_model.__class__.__name__, ('atualizado' if pk else 'salvo')))
                
            for related in self.bind_related:
                post = request.POST.copy()
                post[related.parent_field_name] = str(self.saved_model.pk)
                related_form = related.fetch(parent_instance=self.saved_model, data=post, files=request.FILES)
                related_form.is_valid()
                r = related_form.save()
                messages.success(request, "Objeto {} {} com sucesso".format(r.__class__.__name__,  'gravado'))

            return self.fetch_success_redirect(request, *args, **kwargs, pk_model=self.saved_model.pk)
        else:
            messages.warning(request, "Formulário inválido")
            return self.get(request=request, **{self.formalias: form}, **(dict(tuple_forms_list)), **kwargs)

    def delete(self, request, *args, **kwargs): 
        item = self.model.objects.get(pk=kwargs.get('pkdelete', None))
        pk_parent = (getattr(item, self.parent_field_name)).pk if self.parent_field_name else None

        item_object_name = item.__class__.__name__
        if item:
            item.delete()
            messages.success(request, "Um registro de {} removido com sucesso".format(item_object_name))
        return self.fetch_delete_redirect(request, *args, **kwargs, pk_parent=pk_parent)

    def get_target_child(self, request, *args, **kwargs):

        current_url = resolve(request.path_info).url_name

        for child in self.bind_children:
            if child.match_url(current_url):
                return child
        return None

    def match_url(self, url):

        url_triggers_regex = [re.compile(u) for u in self.url_triggers]
        if any(url_regex.match(url) for url_regex in url_triggers_regex):
            return True

        for child in self.bind_children:
            if child.match_url(url):
                return True

        return False

    def get_children(self):
        b = []
        for class_child in self.children:
            child = class_child()
            child.parent = self
            child.template_name = self.template_name
            if not getattr(child, 'parent_field_name', None):
                child.parent_field_name = self.class_name.lower()
            b.append(child)
        return b

    def get_related(self):
        b = []
        for class_related in self.related:
            related = class_related()
            related.parent = self
            if not getattr(related, 'parent_field_name', None):
                related.parent_field_name = self.class_name.lower()
            b.append(related)
        return b

    def get_pks_parents(self, request, *args, **kwargs):

        pk = self.saved_model.pk if self.saved_model else kwargs.get(self.pkalias, None)

        if self.parent:
            return self.parent.get_pks_parents(request, *args, **kwargs) + [str(pk)]
        else:
            return [str(pk)]

    def fetch_success_redirect(self, request, *args, **kwargs):
        pk = kwargs.get('pk_model', None)
        return redirect(self.success_redirect, pk) if pk else redirect(self.success_redirect)

    def fetch_delete_redirect(self, request, *args, **kwargs):
        pk = kwargs.get('pk_parent', None)
        return redirect(self.delete_redirect, pk) if pk else redirect(self.delete_redirect)


class ModalListView(MainView):

    def fetch_success_redirect(self, request, *args, **kwargs):
        pk = kwargs.get('pk_model', None)
        parent_pk = ((getattr(self.model.objects.get(pk=pk), self.parent_field_name)).pk) if self.parent_field_name else None
        return redirect(self.success_redirect, parent_pk) if parent_pk else redirect(self.success_redirect)

class MainViewStaticAliases(MainView):

    formalias = 'form'
    setalias = 'data'
    pkalias = 'pk'

class ModalListViewStaticAliases(ModalListView):

    formalias = 'form'
    setalias = 'data'
    pkalias = 'pk'
