from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from core.models import Cargo, Entidade, Funcao, Responsavel, Usuario, Bolsista, Documento
from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm

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

def bolsista_handle(request, pk=None, pkdelete=None):
    if request.method == 'POST':
        form = BolsistaForm(request.POST, instance=Bolsista.objects.get(pk=pk)) if pk else BolsistaForm(request.POST)
        if form.is_valid() and form.save():
            return redirect('bolsista')
    elif request.method == 'GET':
        form = BolsistaForm(instance=Bolsista.objects.get(pk=pk)) if pk else BolsistaForm()

    return render(request, 'administracao/bolsista.html', {
        'content_title': 'Cadastrar Bolsistas / Pequisadores',
        'form': form,
        'formf': DocumentoForm()
    })

def upload_arquivo_bolsista(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('bolsista')