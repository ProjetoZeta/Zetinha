from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

from .models import Cargo as CargoModel
from .models import Entidade, Funcao, Responsavel, Usuario, Bolsista, Documento, EmprestimoEquipamento,Projeto
from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm, ProjetoForm, EmprestimoEquipamentoForm
from django.views.generic import View

from django.http import HttpResponse
from django.views import View

import importlib

class GenericEntity(View):
        
    def dispatch(self, request, *args, **kwargs):
        self.class_name = self.__class__.__name__
        self.model_class = getattr(importlib.import_module('cadastro.models'), self.class_name)
        self.form_class = getattr(importlib.import_module('cadastro.forms'), self.class_name+'Form')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        pkdelete = kwargs.get('pkdelete', None)
        if pkdelete:
            return self.delete(request=request, pk=pkdelete)
        else:
            pk = kwargs.get('pk', None)
            form = kwargs.get('form', None)
            if form is None:
                form = self.form_class(instance=self.model_class.objects.get(pk=pk)) if pk else self.form_class()
            if pk:
                form.is_edit = True
            return render(request, 'cadastro/crud-withmodal.html', {
                'data': self.model_class.objects.all(),
                'form': form,
                'content_title': self.model_class._meta.verbose_name_plural.title()
            })

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        form = self.form_class(request.POST, instance=self.model_class.objects.get(pk=pk)) if pk else self.form_class(request.POST)
        if form.is_valid() and form.save():
            return redirect(self.class_name.lower())
        else:
            return self.get(request=request, form=form)

    def delete(self, request, *args, **kwargs):
        item = self.model_class.objects.get(pk=kwargs.get('pk', None))
        if item:
            item.delete()
        return redirect(self.class_name.lower())

class Cargo(GenericEntity):
    pass

class Funcao(GenericEntity):
    pass

class Entidade(GenericEntity):
    pass    

class Responsavel(GenericEntity):
    pass

class Usuario(GenericEntity):
    pass

def main(request):
    return render(request, 'cadastro/foo.html', {})

def projeto(request, pk=None, pkdelete=None):
    if pkdelete:
        item = Projeto.objects.get(pk=pkdelete)
        if item:
            item.delete()
        return redirect('projeto')
    return render(request, 'cadastro/crud-projeto.html', {
        'data': Projeto.objects.all(),
        'form': ProjetoForm(),
        'content_title': 'Projeto'
    })

def bolsista(request, pk=None, pkdelete=None):
    if pkdelete:
        item = Bolsista.objects.get(pk=pkdelete)
        if item:
            item.delete()
        return redirect('bolsista')
    return render(request, 'cadastro/crud-bolsista.html', {
        'data': Bolsista.objects.all(),
        'form': BolsistaForm(),
        'content_title': 'Bolsistas'
    })


def fetch_bolsista(request, bolsista_form, documento_form, emprestimo_form, pk):
    return render(request, 'cadastro/bolsista.html', {
        'content_title': 'Cadastrar Bolsistas / Pequisadores',
        'form': bolsista_form,
        'formf': documento_form,
        'forme': emprestimo_form,
        'documents': Documento.objects.filter(bolsista=Bolsista.objects.get(pk=pk) if pk else None),
        'emprestimos': EmprestimoEquipamento.objects.filter(bolsista=Bolsista.objects.get(pk=pk) if pk else None),
        'projects': Bolsista.objects.get(pk=pk).projeto_atual if pk else 'None',
        'pk': pk
    })

def bolsista_handle(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        form = BolsistaForm(request.POST, instance=Bolsista.objects.get(pk=pk)) if pk else BolsistaForm(request.POST)
        if form.is_valid() and form.save():
            return redirect('bolsista')
    elif request.method == 'GET':
        form = BolsistaForm(instance=Bolsista.objects.get(pk=pk)) if pk else BolsistaForm()
    documento_form = DocumentoForm(initial={'bolsista': Bolsista.objects.get(pk=pk)}) if pk else DocumentoForm()
    documento_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

    emprestimo_equipamento_form = EmprestimoEquipamentoForm(initial={'bolsista': Bolsista.objects.get(pk=pk)}) if pk else EmprestimoEquipamentoForm()
    emprestimo_equipamento_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

    return fetch_bolsista(request, form, documento_form, emprestimo_equipamento_form, pk)

def handle_arquivo_bolsista(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        bolsista = Bolsista.objects.get(pk=request.POST.get('bolsista', None))
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bolsista-editar', pk=bolsista.pk)
        bolsista_form = BolsistaForm(instance=Bolsista.objects.get(pk=bolsista.pk)) if bolsista.pk else BolsistaForm()
    elif request.method == 'GET':
        bolsista = Bolsista.objects.get(pk=Documento.objects.get(pk=pkdelete if pkdelete else pk).bolsista.pk)
        form = DocumentoForm()
        bolsista_form = BolsistaForm(instance=bolsista)
        if pkdelete:
            item = Documento.objects.get(pk=pkdelete)
            if item:
                item.delete()
        return redirect('bolsista-editar', pk=bolsista.pk)
    return fetch_bolsista(request, bolsista_form, form, EmprestimoEquipamentoForm(), bolsista.pk)


def handle_emprestimo_equipamento_bolsista(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        bolsista = Bolsista.objects.get(pk=request.POST.get('bolsista', None))
        form = EmprestimoEquipamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bolsista-editar', pk=bolsista.pk)
        bolsista_form = BolsistaForm(instance=Bolsista.objects.get(pk=bolsista.pk)) if bolsista.pk else BolsistaForm()
    elif request.method == 'GET':
        bolsista = Bolsista.objects.get(pk=EmprestimoEquipamento.objects.get(pk=pkdelete if pkdelete else pk).bolsista.pk)
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
            'document': Documento.objects.get(pk=pk)
        })

def show_emprestimoequipamento(request, pk=None):
    if request.method == 'GET':
        return render(request, 'cadastro/emprestimo-viewer.html', {
            'content_title': 'Empréstimo de Equipamento',
            'emprestimo': EmprestimoEquipamento.objects.get(pk=pk)
        })

def projeto_handle(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=Projeto.objects.get(pk=pk)) if pk else ProjetoForm(request.POST)
        if form.is_valid() and form.save():
            return redirect('projeto')

    elif request.method == 'GET':
        form = ProjetoForm(instance=Projeto.objects.get(pk=pk)) if pk else ProjetoForm()

    return fetch_projeto(request, form, pk)


def fetch_projeto(request, form,  pk):
    return render(request,'cadastro/projeto.html', {
                'content_title': 'Manter Projeto',
                'form': form,
                'pk': pk
                })
