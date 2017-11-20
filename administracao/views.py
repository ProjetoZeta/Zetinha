from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Cargo, Entidade, Funcao, Responsavel, Usuario
from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm

# Create your views here.

def main(request):
    return render(request, 'administracao/cargo.html', {})

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
    return render(request, 'administracao/generic-table.html', {
        'data': globals()[model].objects.all(),
        'form': form
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
