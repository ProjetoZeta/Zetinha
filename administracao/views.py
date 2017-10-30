from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from administracao.models import Entidade
from administracao.forms import UserForm
from utils.views import translate_model

from .models import Cargo
from .models import Entidade

# Create your views here.

def main(request):
    return render(request, 'administracao/main.html', {})


def cargo(request):
    return render(request, 'administracao/generic-table.html', translate_model(Cargo))

def entidade(request):
    return render(request, 'administracao/generic-table.html', translate_model(Entidade))

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        return HttpResponseRedirect('/contact/thanks/')
    else:
        form = UserForm()
    template = get_template('administracao/usuario.html')
    html = template.render({'form': form})
    return HttpResponse(html)
