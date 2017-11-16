from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.urls import reverse_lazy

# Create your views here.

def main(request):
    return render(request, 'usuario/bolsista.html', {})


