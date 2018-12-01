from django.shortcuts import render
from cadastro.models import Bolsista
from django.utils import timezone


def schedule(request):
    return render(request,'relatorio/schedule.html')


def declaracao_residencia(request, pk):
    bolsista = Bolsista.objects.get(pk=pk)
    today = timezone.now()
    params = {
            'today': today,
            'bolsista': bolsista,
            'request': request
        }

    return render(request,'relatorio/residencia.html', params)

def declaracao_bolsa(request, pk):
    bolsista = Bolsista.objects.get(pk=pk)
    today = timezone.now()
    params = {
            'today': today,
            'bolsista': bolsista,
            'request': request
        }

    return render(request,'relatorio/declaracao-bolsista.html', params)

def declaracao_sigilo(request, pk):
    bolsista = Bolsista.objects.get(pk=pk)
    today = timezone.now()
    params = {
            'today': today,
            'bolsista': bolsista,
            'request': request
        }

    return render(request,'relatorio/declaracao-sigilo.html', params)