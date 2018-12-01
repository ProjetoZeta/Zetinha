from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'residencia/(?P<pk>[0-9]+)$', views.declaracao_residencia,name='relatorio-gerar-residencia'),
    url(r'ciencia-bolsa/(?P<pk>[0-9]+)$', views.declaracao_bolsa,name='relatorio-gerar-ciencia-bolsista'),
    url(r'sigilo/(?P<pk>[0-9]+)$', views.declaracao_sigilo,name='relatorio-gerar-sigilo'),
    url(r'schedule$', views.schedule,name='schedule-atividades'),
]
