from django.shortcuts import render
from cadastro.models import Bolsista, Meta, Projeto 
from django.utils import timezone
from django.http import JsonResponse


def schedule_data(request, pkprojeto):
    projeto = Projeto.objects.get(pk=pkprojeto)
    metas = Meta.objects.filter(projeto=projeto, ic_ativo=True).order_by('posicao')
    data = []
    for meta in metas:
        atividades = meta.atividade_set.filter(ic_ativo=True).order_by('posicao')
        tasks = []
        for atividade in atividades:
            tasks.append({'title': atividade.titulo, 'id': atividade.pk, 'initial_date': atividade.data_inicio, 'end_date': atividade.data_fim, 'posicao': atividade.posicao})
        data.append({'title': meta.titulo, 'id': meta.pk, 'posicao': meta.posicao, 'tasks': tasks})

    return JsonResponse(dict({'data': data}))


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