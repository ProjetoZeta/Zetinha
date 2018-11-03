from django.views import View

from django.shortcuts import render, redirect

import importlib

class GenericView(View):
        
    template_keys = {}

    def dispatch(self, request, *args, **kwargs):

        if not hasattr(self, 'model'):
            self.model = getattr(importlib.import_module('cadastro.models'), self.__class__.__name__)
        
        self.class_name = self.model.__name__

        if not hasattr(self, 'form'):
            self.form = getattr(importlib.import_module('cadastro.forms'), self.class_name+'Form')

        if not hasattr(self, 'sucess_redirect'):
            self.sucess_redirect = self.class_name.lower()
        
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        pkdelete = kwargs.get('pkdelete', None)
        if pkdelete:
            return self.delete(request=request, pk=pkdelete)
        else:
            pk = kwargs.get('pk', None)
            form = kwargs.get('form', None)
            if form is None:
                form = self.form(instance=self.model.objects.get(pk=pk)) if pk else self.form()
            if pk:
                form.is_edit = True
            return render(request, self.template_name, {
                'data': self.model.objects.all(),
                'form': form,
                'content_title': self.model._meta.verbose_name_plural.title(),
                **self.template_keys
            })

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        form = self.form(request.POST, instance=self.model.objects.get(pk=pk)) if pk else self.form(request.POST)
        if form.is_valid() and form.save():
            return redirect(self.sucess_redirect)
        else:
            return self.get(request=request, form=form)

    def delete(self, request, pk):
        item = self.model.objects.get(pk=pk)
        if item:
            item.delete()
        return redirect(self.sucess_redirect)

    def save(self, request, form):
        pass

    def fetch():
        pass