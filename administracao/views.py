from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from administracao.models import Entidade
from administracao.forms import UserForm
from utils.views import get_data_for_generic_table

from .models import Cargo, Entidade, Funcao

from .forms import CargoForm, EntidadeForm, FuncaoForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def main(request):
    return render(request, 'administracao/main.html', {})

def cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo')
    else:
        form = CargoForm()
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Cargo),
        'form': form
    })

def funcao(request):
    if request.method == 'POST':
        form = FuncaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcao')
    else:
        form = FuncaoForm()
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Funcao),
        'form': form
    })

def entidade(request):
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Entidade),
        'form': EntidadeForm()
    })

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        return HttpResponseRedirect('/contact/thanks/')
    else:
        form = UserForm()
    template = get_template('administracao/usuario.html')
    html = template.render({'form': form})
    return HttpResponse(html)
