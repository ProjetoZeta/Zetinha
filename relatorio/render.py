from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from cadastro.models import Bolsista

from django import template

class Render:

	@staticmethod
	def render(path: str, params: dict):
		template = get_template(path)
		html = template.render(params)
		response = BytesIO()
		pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
		if not pdf.err:
			return HttpResponse(response.getvalue(), content_type='application/pdf')
		else:
			return HttpResponse("Error Rendering PDF", status=400)

	@staticmethod
	def text(text: str, context: dict):

		context = template.Context(context)
		t = template.Template(text)
		return t.render(context)


	@staticmethod
	def bolsista_dict(pk):
		bolsista = Bolsista.objects.get(pk=pk)
		participacoes = bolsista.participante_set.filter(ic_ativo=True)
		participante = participacoes.first() if participacoes.count() else None
		projeto = participante.projeto if participante else None

		return {
			'bolsista': bolsista,
			'projeto': projeto,
			'participante': participante,
		}