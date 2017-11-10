from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from utils.views import get_data_for_generic_table

from .models import Cargo, Entidade, Funcao, Responsavel, Usuario

from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm

# Create your views here.

def main(request):
    return render(request, 'administracao/main.html', {})

def cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.method == 'GET':
        form = CargoForm()
        
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Cargo),
        'form': form
    })

class CargoDelete(DeleteView):
    model = Cargo
    success_url = reverse_lazy('administracao:cargo')
    def get_success_url(self):
        return reverse('your_redirect_view')

def funcao(request):
    if request.method == 'POST':
        form = FuncaoForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.method == 'GET':
        form = FuncaoForm()
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Funcao),
        'form': form
    })

def entidade(request):
    if request.method == 'POST':
        form = EntidadeForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.method == 'GET':
        form = EntidadeForm()
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Entidade),
        'form': form
    })

def responsavel(request):
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.method == 'GET':
        form = ResponsavelForm()
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Responsavel),
        'form': form
    })

def usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.method == 'GET':
        form = UsuarioForm()
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Usuario, fields=['email', 'no_completo', 'ic_ativo', 'ic_bolsista']),
        'form': form
    })
