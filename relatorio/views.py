from django.shortcuts import render
from cadastro.models import Bolsista, Meta, Projeto 
from .forms import ParticipantesSelect
from django.utils import timezone
from django.http import JsonResponse, HttpResponse

from relatorio.render import Render, Relatorio
from relatorio.msoffice import Word, Excel

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

def docx_sigilo(request, pk):

	template_name = 'Formulario_declaracao_de_sigilo.docx'
	
	docx = Word(template_name, Render.bolsista_dict(pk=pk))

	return docx.update_and_download()

def docx_declaracao_residencia(request, pk):

	template_name = 'DECLARAÇÃO_DE_COMPROVAÇÃO_DE_RESIDÊNCIA.docx'

	docx = Word(template_name, Render.bolsista_dict(pk=pk))

	return docx.update_and_download()

def xlsx_termo_compromisso(request, pk):

	template_name = 'Termo_de_Compromisso_de_Bolsista.xlsx'
	
	xlsx = Excel(template_name, Render.bolsista_dict(pk=pk))

	return xlsx.update_and_download()

def relatorios(request):

	return render(request, 'relatorio/relatorios.html', {'content_title': 'Gerar Relatórios', 'projetos': Projeto.objects.all(), 'tipos': Relatorio.TIPOS})

def get_participantes(self, pk):
    form = ParticipantesSelect(pkprojeto=pk)
    return HttpResponse(form)