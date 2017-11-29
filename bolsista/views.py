from django.shortcuts import render

def main(request):
    return render(request, 'bolsista/teste.html', {})


def meuperfil(request):
	return render(request, 'bolsista/meuperfil.html', {'content_title':'Atualize seus dados'})