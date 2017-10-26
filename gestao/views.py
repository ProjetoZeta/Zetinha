from django.template.loader import get_template
from django.http import HttpResponse

from gestao.models import Entidade

# Create your views here.
class WebLoader:
    def main(request):
        template = loader.get_template('gestao/main.html')
        context = {}
        return HttpResponse(template.render(context, request))

    def user(request):
        userData = RetrieveData.retrieveUsers
        template = get_template('gestao/usuario.html')
        html = template.render({'users': userData})
        return HttpResponse(html)

class RetrieveData:
    def retrieveUsers:
        dataList = Entidade.objects.all()
        return dataList
