from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from administracao.models import Entidade
from administracao.forms import UserForm
from utils.views import get_data_for_generic_table

from .models import Cargo
from .models import Entidade

from .forms import CargoForm, EntidadeForm

# Create your views here.

def main(request):
    return render(request, 'administracao/main.html', {})

def cargo(request):
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Cargo),
        'create_form': CargoForm()
    })

def entidade(request):
    return render(request, 'administracao/generic-table.html', {
        'data': get_data_for_generic_table(Entidade),
        'create_form': EntidadeForm()
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
