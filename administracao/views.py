from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from administracao.models import Entidade
from administracao.forms import UserForm

# Create your views here.

def main(request):
    return render(request, 'administracao/main.html', {})


def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        return HttpResponseRedirect('/contact/thanks/')
    else:
        form = UserForm()
    template = get_template('administracao/usuario.html')
    html = template.render({'form': form})
    return HttpResponse(html)
