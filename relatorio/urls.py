from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'residencia/(?P<pk>[0-9]+)$', views.declaracao_residencia,name='relatorio-gerar-residencia'),
    url(r'ciencia-bolsa/(?P<pk>[0-9]+)$', views.declaracao_bolsa,name='relatorio-gerar-ciencia-bolsista'),
    url(r'sigilo/(?P<pk>[0-9]+)$', views.declaracao_sigilo,name='relatorio-gerar-sigilo'),
    url(r'cronograma/(?P<pkprojeto>[0-9]+)$', views.schedule_data,name='schedule-atividades'),

    url(r'sigilodocx/(?P<pk>[0-9]+)$', views.docx_sigilo,name='relatorio-gerar-doc-sigilo'),
    url(r'termocompromissoxlsx/(?P<pk>[0-9]+)$', views.xlsx_termo_compromisso,name='relatorio-gerar-xlsx-tc'),
    url(r'declaracaoresidenciadocx/(?P<pk>[0-9]+)$', views.docx_declaracao_residencia,name='relatorio-residencia-xlsx'),

    url(r'^$', views.relatorios, name='relatorios'),
]
