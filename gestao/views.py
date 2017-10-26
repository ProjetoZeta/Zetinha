from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect

from gestao.models import Entidade
from gestao.forms import UserForm

# Create your views here.

def main(request):
    template = loader.get_template('gestao/main.html')
    context = {}
    return HttpResponse(template.render(context, request))

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        return HttpResponseRedirect('/contact/thanks/')
    else:
        form = UserForm()
    template = get_template('gestao/usuario.html')
    html = template.render({'form': form})
    return HttpResponse(html)
