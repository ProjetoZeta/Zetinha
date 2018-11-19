from django.views import View

from django.shortcuts import render, redirect

import importlib

from django.urls import resolve

from django.contrib import messages

import re

class MainView(View):

    children = []
    url_triggers = []
    parent = None
    saved_model = None
    formalias = None
    setalias = None
    pkalias = None

    def __init__(self, **kwargs):

        self.class_name = self.model.__name__
        self.form = getattr(importlib.import_module('cadastro.forms'), self.class_name+'Form')
        self.bind_children = self.get_children()
        if not getattr(self, 'pkalias', None):
            self.pkalias = 'pk{}'.format(self.class_name.lower())
        if not getattr(self, 'formalias', None):
            self.formalias = "form{}".format(self.class_name.lower())
        if not getattr(self, 'setalias', None):
            self.setalias = "set{}".format(self.class_name.lower())

        super().__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):

        child_target = self.get_target_child(request, *args, **kwargs)

        if child_target:
            return child_target.dispatch(request, *args, **kwargs)
        #elif not self.pkalias in [*kwargs]:
        #    return "erro aki"

        pkdelete = kwargs.get('pkdelete', None)
        if pkdelete:
            return self.delete(request=request, *args, **kwargs)

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:        
            handler = self.http_method_not_allowed

        return handler(request, *args, **kwargs)

    def fetch_template_keys(self, request, *args, **kwargs):

        parent_view_model_name = self.parent.class_name.lower() if self.parent else None
        pk = kwargs.get(self.pkalias, None)

        parent_pk = kwargs.get(self.parent.pkalias, None) if self.parent else None

        parent_reference = {parent_view_model_name: parent_pk} if parent_view_model_name and parent_pk else None
        model_instance = self.model.objects.get(pk=pk) if pk else None          

        passed_form_error = kwargs.get(self.formalias, None)

        if passed_form_error:
            form = passed_form_error
        else:
            form = self.form(initial=parent_reference, instance=model_instance)


        model_set = self.model.objects.filter(**parent_reference) if parent_reference else self.model.objects.all()

        children_tuple_template_keys = []

        for child in self.bind_children:

            model = self.model(pk=pk) if pk else None
            field = self.class_name.lower()

            set_child = child.model.objects.filter(**{field: model}) if model else []

            form_child_initial = {self.class_name.lower(): model} if model else None

            children_tuple_template_keys.append( (child.formalias, child.form(initial=form_child_initial), ) )
            children_tuple_template_keys.append( (child.setalias, set_child, ) )

        parent_template_keys = self.parent.fetch_template_keys(request, *args, **kwargs) if self.parent else {}

        return {
            **parent_template_keys,
            **(dict(children_tuple_template_keys)),
            self.formalias: form,
            self.setalias: model_set,
            self.pkalias: pk,
            **self.template_keys(request, *args, **kwargs)
        }

    def template_keys(self, request, *args, **kwargs):
        return {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            **self.fetch_template_keys(request, *args, **kwargs)
        })

    def post(self, request, *args, **kwargs):

        pk = kwargs.get(self.pkalias, None)
        model_instance = self.model.objects.get(pk=pk) if pk else None 

        form = self.form(request.POST, instance=model_instance)
        if form.is_valid():
            self.saved_model = form.save()
            messages.success(request, "Objeto {} {} com sucesso".format(self.saved_model.__class__.__name__, ('atualizado' if pk else 'salvo')))
            return self.fetch_success_redirect(request, *args, **kwargs)
        else:
            messages.warning(request, "Formulário inválido")
            return self.get(request=request, **{self.formalias: form}, **kwargs)

    def delete(self, request, *args, **kwargs):
        item = self.model.objects.get(pk=kwargs.get('pkdelete', None))
        if item:
            item.delete()
        return self.fetch_delete_redirect(request, *args, **kwargs)

    def get_target_child(self, request, *args, **kwargs):

        current_url = resolve(request.path_info).url_name

        for child in self.bind_children:
            url_triggers_regex = [re.compile(url) for url in child.url_triggers]
            if any(url_regex.match(current_url) for url_regex in url_triggers_regex):
                return child

        return None

    def set_template_name(self, template_name):
        self.template_name = template_name

    def set_parent(self, parent):
        self.parent = parent

    def get_children(self):
        b = []
        for class_child in self.children:
            child = class_child()
            child.set_parent(self)
            child.set_template_name(self.template_name)
            b.append(child)
        return b

    def get_pks_parents(self, request, *args, **kwargs):

        pk = self.saved_model.pk if self.saved_model else kwargs.get(self.pkalias, None)

        if self.parent:
            return self.parent.get_pks_parents(request, *args, **kwargs) + [str(pk)]
        else:
            return [str(pk)]

    def fetch_success_redirect(self, request, *args, **kwargs):
        pks_branch_list = self.get_pks_parents(request, *args, **kwargs)
        return redirect(self.success_redirect, *(tuple(pks_branch_list)))

    def fetch_delete_redirect(self, request, *args, **kwargs):
        pks_branch_list = self.get_pks_parents(request, *args, **kwargs)
        pks_branch_list.pop()
        return redirect(self.delete_redirect, *(tuple(pks_branch_list)))


class ModalListView(MainView):

    def fetch_success_redirect(self, request, *args, **kwargs):
        pks_branch_list = self.get_pks_parents(request, *args, **kwargs)
        pks_branch_list.pop()
        return redirect(self.success_redirect, *(tuple(pks_branch_list)))



class GenericView(View):

    pk_alias = 'pk'

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        if not hasattr(self, 'model'):
            self.model = getattr(importlib.import_module('cadastro.models'), self.__class__.__name__)
        
        self.class_name = self.model.__name__

        self.save_redirect = (self.class_name.lower(),)

        self.delete_redirect = (self.class_name.lower(),)


    def delete(self, request, **kwargs):
        item = self.model.objects.get(pk=kwargs.get('pkdelete', None))
        if item:
            item.delete()
        return redirect(*self.delete_redirect)

    def get(self, request, **kwargs):

        pkdelete = kwargs.get('pkdelete', None)
        if pkdelete:
            return self.delete(request=request, **kwargs)
        else:
            return render(request, self.template_name, {
                **self.template_keys(**kwargs)
            })

    def template_keys(self, **kwargs):
        return {}

class FormView(GenericView):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.form = getattr(importlib.import_module('cadastro.forms'), self.class_name+'Form')

    def post(self, request, **kwargs):

        pk = kwargs.get(self.pk_alias, None)

        form = self.form(request.POST, instance=self.model.objects.get(pk=pk)) if pk else self.form(request.POST)
        if form.is_valid() and form.save():
            return redirect(*self.save_redirect)
        else:
            return self.get(request=request, form=form, **kwargs)

    def template_keys(self, **kwargs):

        pk = kwargs.get(self.pk_alias, None)
        form = kwargs.get('form', None)
        if form is None:
            form = self.form(instance=self.model.objects.get(pk=pk)) if pk else self.form()
        if pk:
            form.is_edit = True

        return {
            **super().template_keys(**kwargs),
            'data': self.model.objects.all(),
            'form': form,
            'content_title': self.model._meta.verbose_name_plural.title(),
            'pk': pk if pk else None,
        }


