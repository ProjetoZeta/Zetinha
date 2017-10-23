from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def felipe(request):
    template = loader.get_template('gestao/main.html')
    context = {}
    return HttpResponse(template.render(context, request))

def fuck(request):
    template = loader.get_template('gestao/usuario.html')
    context = {}
    return HttpResponse(template.render(context, request))