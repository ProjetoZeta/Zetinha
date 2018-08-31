from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

from core.models import Cargo, Entidade, Funcao, Responsavel, Usuario, Bolsista, Documento, Projeto, EmprestimoEquipamento,ProjetoDenominacao, ProjetoInteressados, ProjetoMetas
from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm, ProjetoForm, ProjetoDenominacaoForm, EmprestimoEquipamentoForm, ProjetoInteressadosForm, ProjetoMetasForm
from .render import Render
from django.views.generic import View
from django.utils import timezone

# Create your views here.

def main(request):
    return render(request, 'administracao/foo.html', {})

def handler(model, request, pk, pkdelete):
    if pkdelete:
        item = globals()[model].objects.get(pk=pkdelete)
        if item:
            item.delete()
        return redirect(model.lower())
    if request.method == 'POST':
        form = globals()[model+'Form'](request.POST, instance=globals()[model].objects.get(pk=pk)) if pk else globals()[model+'Form'](request.POST)
        if form.is_valid() and form.save():
            return redirect(model.lower())
    elif request.method == 'GET':
        form = globals()[model+'Form'](instance=globals()[model].objects.get(pk=pk)) if pk else globals()[model+'Form']()
    if pk:
        form.is_edit = True
    return render(request, 'administracao/crud-withmodal.html', {
        'data': globals()[model].objects.all(),
        'form': form,
        'content_title': globals()[model]._meta.verbose_name_plural.title()
    })

def cargo(request, pk=None, pkdelete=None):
    return handler("Cargo", request, pk, pkdelete)

def funcao(request, pk=None, pkdelete=None):
    return handler("Funcao", request, pk, pkdelete)

def entidade(request, pk=None, pkdelete=None):
    return handler("Entidade", request, pk, pkdelete)

def responsavel(request, pk=None, pkdelete=None):
    return handler("Responsavel", request, pk, pkdelete)

def usuario(request, pk=None, pkdelete=None):
    return handler("Usuario", request, pk, pkdelete)

def projeto(request, pk=None, pkdelete=None):
    if pkdelete:
        item = Bolsista.objects.get(pk=pkdelete)
        if item:
            item.delete()
        return redirect('projeto')
    return render(request, 'administracao/crud-projeto.html', {
        'data': ProjetoDenominacao.objects.all(),
        'form': ProjetoDenominacaoForm(),
        'content_title': 'Projeto'
    })

def bolsista(request, pk=None, pkdelete=None):
    if pkdelete:
        item = Bolsista.objects.get(pk=pkdelete)
        if item:
            item.delete()
        return redirect('bolsista')
    return render(request, 'administracao/crud-bolsista.html', {
        'data': Bolsista.objects.all(),
        'form': BolsistaForm(),
        'content_title': 'Bolsistas'
    })


def fetch_bolsista(request, bolsista_form, documento_form, emprestimo_form, pk):
    return render(request, 'administracao/bolsista.html', {
        'content_title': 'Cadastrar Bolsistas / Pequisadores',
        'form': bolsista_form,
        'formf': documento_form,
        'forme': emprestimo_form,
        'documents': Documento.objects.filter(bolsista=Bolsista.objects.get(pk=pk) if pk else None),
        'emprestimos': EmprestimoEquipamento.objects.filter(bolsista=Bolsista.objects.get(pk=pk) if pk else None),
        'projects': Bolsista.objects.get(pk=1).projeto_atual if pk else 'None',
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
        return render(request, 'common/file-viewer.html', {
            'content_title': 'Preview de arquivo',
            'document': Documento.objects.get(pk=pk)
        })

def show_emprestimoequipamento(request, pk=None):
    if request.method == 'GET':
        return render(request, 'administracao/emprestimo-viewer.html', {
            'content_title': 'Empréstimo de Equipamento',
            'emprestimo': EmprestimoEquipamento.objects.get(pk=pk)
        })

def projeto_handle(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        form_denominacao = ProjetoDenominacaoForm(request.POST, instance=ProjetoDenominacao.objects.get(pk=pk)) if pk else ProjetoDenominacaoForm(request.POST)
        form_interessados = ProjetoInteressadosForm(request.POST, instance=ProjetoInteressados.objects.get(pk=pk)) if pk else ProjetoInteressadosForm(request.POST)
        form_metas = ProjetoMetasForm(request.POST, instance=ProjetoMetas.objects.get(pk=pk)) if pk else ProjetoMetasForm(request.POST)

        if form.is_valid() and form.save():
            return redirect('projeto')
    elif request.method == 'GET':
        form_denominacao = ProjetoDenominacaoForm(instance=ProjetoDenominacao.objects.get(pk=pk)) if pk else ProjetoDenominacaoForm()
        form_interessados = ProjetoInteressadosForm(instance=ProjetoInteressados.objects.get(pk=pk)) if pk else ProjetoInteressadosForm()
        form_metas = ProjetoMetasForm(instance=ProjetoMetas.objects.get(pk=pk)) if pk else ProjetoMetasForm()

    return fetch_projeto(request, form_denominacao, form_interessados, form_metas, pk)


def fetch_projeto(request, form_denominacao, form_interessados, form_metas, pk):
    return render(request,'administracao/projeto2.html', {
                'content_title': 'Manter Projeto',
                'form_denominacao': form_denominacao,
                'form_interessados': form_interessados,
                'form_metas': form_metas,
                'pk': pk
                })

class Pdf(View):

    def get(self, request):
        bolsistas = Bolsista.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'bolsistas': bolsistas,
            'request': request
        }

        return Render.render('pdf.html', params)
