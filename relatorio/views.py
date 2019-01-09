from django.shortcuts import render
from cadastro.models import Bolsista, Meta, Projeto 
from django.utils import timezone
from django.http import JsonResponse, HttpResponse

from relatorio.render import Render
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

def doc_sigilo2(request, pk):

	template_name = 'file.docx'
	doc = Word(template_name)

	bolsista = Bolsista.objects.get(pk=pk)
	participacoes = bolsista.participante_set.filter(ic_ativo=True)
	projeto = participacoes.first().projeto if participacoes.count() else None

	processed_text = Render.text(doc.get_text_content(), {
		'bolsista': bolsista,
		'projeto': projeto
		})
	return doc.update_and_download(data=processed_text)

def doc_sigilo3(request, pk):

	template_name = 'file.docx'
	doc = Word(template_name)

	bolsista = Bolsista.objects.get(pk=pk)
	participacoes = bolsista.participante_set.filter(ic_ativo=True)
	projeto = participacoes.first().projeto if participacoes.count() else None

	processed_text = Render.text(doc.get_text_content(), {
		'bolsista': bolsista,
		'projeto': projeto
		})
	return doc.update_and_download(data=processed_text)

def doc_sigilo(request, pk):

	bolsista = Bolsista.objects.get(pk=pk)
	return DocRenderer('relatorio/templates/relatorio/file.docx').render({'bolsista': bolsista})