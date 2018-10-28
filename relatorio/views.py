from django.shortcuts import render
from cadastro.models import Bolsista
from django.utils import timezone

# Create your views here.


def declaracao_residencia(request, pk):
    bolsista = Bolsista.objects.get(pk=pk)
    today = timezone.now()
    params = {
            'today': today,
            'bolsista': bolsista,
            'request': request
        }

    return render(request,'residencia.html', params)

def declaracao_bolsa(request, pk):
    bolsista = Bolsista.objects.get(pk=pk)
    today = timezone.now()
    params = {
            'today': today,
            'bolsista': bolsista,
            'request': request
        }

    return render(request,'declaracao-bolsista.html', params)

def declaracao_sigilo(request, pk):
    bolsista = Bolsista.objects.get(pk=pk)
    today = timezone.now()
    params = {
            'today': today,
            'bolsista': bolsista,
            'request': request
        }

    return render(request,'declaracao-sigilo.html', params)