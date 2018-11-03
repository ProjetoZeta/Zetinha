from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

from .models import Cargo as CargoModel, Entidade as EntidadeModel, Funcao as FuncaoModel, Usuario as  UsuarioModel, Bolsista as BolsistaModel, Documento as DocumentoModel, EmprestimoEquipamento as EmprestimoEquipamentoModel, Projeto as ProjetoModel
from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm, ProjetoForm, EmprestimoEquipamentoForm
from django.views.generic import View

from django.http import HttpResponse
from django.views import View

import importlib

class GenericEntity(View):
        
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

    def delete(self, request, *args, **kwargs):
        item = self.model.objects.get(pk=kwargs.get('pk', None))
        if item:
            item.delete()
        return redirect(self.sucess_redirect)

class Cargo(GenericEntity):
    template_name = 'cadastro/crud-withmodal.html'
    template_keys = {'content_title': 'shit'}

class Funcao(GenericEntity):
    template_name = 'cadastro/crud-withmodal.html'

class Entidade(GenericEntity):
    template_name = 'cadastro/crud-withmodal.html'

class Responsavel(GenericEntity):
    template_name = 'cadastro/crud-withmodal.html'

class Usuario(GenericEntity):
    template_name = 'cadastro/crud-withmodal.html'

def main(request):
    return render(request, 'cadastro/foo.html', {})

def projeto(request, pk=None, pkdelete=None):
    if pkdelete:
        item = ProjetoModel.objects.get(pk=pkdelete)
        if item:
            item.delete()
        return redirect('projeto')
    return render(request, 'cadastro/crud-projeto.html', {
        'data': ProjetoModel.objects.all(),
        'form': ProjetoForm(),
        'content_title': 'Projeto'
    })

class Projeto(GenericEntity):

    template_name = 'cadastro/projeto.html'

class ProjetoList(GenericEntity):
    
    model = ProjetoModel
    template_name = 'cadastro/crud-projeto.html'


class Bolsista(GenericEntity):

    template_name = 'cadastro/bolsista.html'

    def dispatch(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        documento_form = DocumentoForm(initial={'bolsista': BolsistaModel.objects.get(pk=pk)}) if pk else DocumentoForm()
        documento_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

        emprestimo_form = EmprestimoEquipamentoForm(initial={'bolsista': BolsistaModel.objects.get(pk=pk)}) if pk else EmprestimoEquipamentoForm()
        emprestimo_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

        self.template_keys = {
            'content_title': 'Cadastrar Bolsistas / Pequisadores',
            'formf': documento_form,
            'forme': emprestimo_form,
            'documents': DocumentoModel.objects.filter(bolsista=BolsistaModel.objects.get(pk=pk) if pk else None),
            'emprestimos': EmprestimoEquipamentoModel.objects.filter(bolsista=BolsistaModel.objects.get(pk=pk) if pk else None),
            'projects': BolsistaModel.objects.get(pk=pk).projeto_atual if pk else None,
            'pk': pk
        }

        return super().dispatch(request, *args, **kwargs)

class BolsistaList(GenericEntity):

    model = BolsistaModel
    template_name = 'cadastro/crud-bolsista.html'

def handle_arquivo_bolsista(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        bolsista = BolsistaModel.objects.get(pk=request.POST.get('bolsista', None))
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bolsista-editar', pk=bolsista.pk)
        bolsista_form = BolsistaForm(instance=BolsistaModel.objects.get(pk=bolsista.pk)) if bolsista.pk else BolsistaForm()
    elif request.method == 'GET':
        bolsista = BolsistaModel.objects.get(pk=DocumentoModel.objects.get(pk=pkdelete if pkdelete else pk).bolsista.pk)
        form = DocumentoForm()
        bolsista_form = BolsistaForm(instance=bolsista)
        if pkdelete:
            item = DocumentoModel.objects.get(pk=pkdelete)
            if item:
                item.delete()
        return redirect('bolsista-editar', pk=bolsista.pk)
    return fetch_bolsista(request, bolsista_form, form, EmprestimoEquipamentoForm(), bolsista.pk)


def handle_emprestimo_equipamento_bolsista(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        bolsista = BolsistaModel.objects.get(pk=request.POST.get('bolsista', None))
        form = EmprestimoEquipamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bolsista-editar', pk=bolsista.pk)
        bolsista_form = BolsistaForm(instance=BolsistaModel.objects.get(pk=bolsista.pk)) if bolsista.pk else BolsistaForm()
    elif request.method == 'GET':
        bolsista = BolsistaModel.objects.get(pk=EmprestimoEquipamento.objects.get(pk=pkdelete if pkdelete else pk).bolsista.pk)
        form = DocumentoForm()
        bolsista_form = BolsistaForm(instance=bolsista)
        if pkdelete:
            item = EmprestimoEquipamento.objects.get(pk=pkdelete)
            if item:
                item.delete()
        return redirect('bolsista-editar', pk=bolsista.pk)
    return fetch_bolsista(request, bolsista_form, DocumentoForm(), form, bolsista.pk)

def show_document(request, pk=None):
    if request.method == 'GET':
        return render(request, 'cadastro/file-viewer.html', {
            'content_title': 'Preview de arquivo',
            'document': DocumentoModel.objects.get(pk=pk)
        })

def show_emprestimoequipamento(request, pk=None):
    if request.method == 'GET':
        return render(request, 'cadastro/emprestimo-viewer.html', {
            'content_title': 'Empréstimo de Equipamento',
            'emprestimo': EmprestimoEquipamento.objects.get(pk=pk)
        })

def projeto_handle(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=ProjetoModel.objects.get(pk=pk)) if pk else ProjetoForm(request.POST)
        if form.is_valid() and form.save():
            return redirect('projeto')

    elif request.method == 'GET':
        form = ProjetoForm(instance=ProjetoModel.objects.get(pk=pk)) if pk else ProjetoForm()

    return fetch_projeto(request, form, pk)


def fetch_projeto(request, form,  pk):
    return render(request,'cadastro/projeto.html', {
                'content_title': 'Manter Projeto',
                'form': form,
                'pk': pk
                })
