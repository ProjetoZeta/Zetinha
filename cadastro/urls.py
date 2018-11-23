from django.conf.urls import url
from django.urls import include, path
from . import views
# from administracao.views import Pdf

urlpatterns = [
    
    url(r'^entidade$', views.EntidadeList.as_view(), name='entidade'),
    url(r'^entidade/novo$', views.Entidade.as_view(), name='entidade-criar'),
    url(r'^entidade/(?P<pkentidade>[0-9]+)/editar$', views.Entidade.as_view(), name='entidade-editar'),
    url(r'^entidade/(?P<pkdelete>[0-9]+)/remover$', views.Entidade.as_view(), name='entidade-remover'),

    url(r'^entidade/(?P<pkentidade>[0-9]+)/responsabilidade/novo$', views.Entidade.as_view(), name='responsabilidade-entidade-criar'),
    url(r'^entidade/(?P<pkentidade>[0-9]+)/responsabilidade/(?P<pkresponsabilidade>[0-9]+)/editar$', views.Entidade.as_view(), name='responsabilidade-entidade-editar'),
    url(r'^entidade/(?P<pkentidade>[0-9]+)/responsabilidade/(?P<pkdelete>[0-9]+)/remover$', views.Entidade.as_view(), name='responsabilidade-entidade-remover'),

    url(r'^emprego$', views.Emprego.as_view(), name='emprego'),
    url(r'^emprego/(?P<pk>[0-9]+)/editar$', views.Emprego.as_view(), name='emprego-editar'),
    url(r'^emprego/(?P<pkdelete>[0-9]+)/remover$', views.Emprego.as_view(), name='emprego-remover'),

    url(r'^responsavel$', views.ResponsavelList.as_view(), name='responsavel'),
    url(r'^responsavel/novo$', views.Responsavel.as_view(), name='responsavel-criar'),
    url(r'^responsavel/(?P<pkresponsavel>[0-9]+)/editar$', views.Responsavel.as_view(), name='responsavel-editar'),
    url(r'^responsavel/(?P<pkdelete>[0-9]+)/remover$', views.Responsavel.as_view(), name='responsavel-remover'),

    url(r'^usuario$', views.Usuario.as_view(), name='usuario'),
    url(r'^usuario/(?P<pk>[0-9]+)/editar$', views.Usuario.as_view(), name='usuario-editar'),
    url(r'^usuario/(?P<pkdelete>[0-9]+)/remover$', views.Usuario.as_view(), name='usuario-remover'),

    url(r'^bolsista$', views.BolsistaList.as_view(), name='bolsista'),
    url(r'^bolsista/novo$', views.Bolsista.as_view(), name='bolsista-criar'),
    url(r'^bolsista/(?P<pk>[0-9]+)/editar$', views.Bolsista.as_view(), name='bolsista-editar'),
    url(r'^bolsista/(?P<pkdelete>[0-9]+)/remover$', views.Bolsista.as_view(), name='bolsista-remover'),

    url(r'^bolsista/(?P<pk>[0-9]+)/arquivo_upload$', views.Bolsista.as_view(), name='upload-arquivo-bolsista'),
    url(r'^bolsista/(?P<pk>[0-9]+)/arquivo/(?P<pkdelete>[0-9]+)/remover$', views.Bolsista.as_view(), name='remover-arquivo-bolsista'),

    url(r'^bolsista/(?P<pk>[0-9]+)/emprestimoequipamento$', views.Bolsista.as_view(), name='emprestimo-equipamento-bolsista'),
    url(r'^bolsista/(?P<pk>[0-9]+)/emprestimoequipamento/(?P<pkdelete>[0-9]+)/remover$', views.Bolsista.as_view(), name='remover-emprestimo-equipamento-bolsista'),

    url(r'documento/(?P<pk>[0-9]+)', views.Documento.as_view(), name='show-document'),

    url(r'emprestimo/(?P<pk>[0-9]+)', views.EmprestimoEquipamento.as_view(), name='show-emprestimoequipamento'),

    url(r'^projeto$', views.ProjetoList.as_view(), name='projeto'),
    url(r'^projeto/novo$', views.Projeto.as_view(), name='projeto-criar'),
    url(r'^projeto/(?P<pk>[0-9]+)/editar$', views.Projeto.as_view(), name='projeto-editar'),
    url(r'^projeto/(?P<pkdelete>[0-9]+)/remover$', views.Projeto.as_view(), name='projeto-remover'),

    url(r'^projeto/(?P<pk>[0-9]+)/participante/novo$', views.Projeto.as_view(), name='participante-proj-criar'),
    url(r'^projeto/(?P<pk>[0-9]+)/participante/(?P<pkparticipante>[0-9]+)/editar$', views.Projeto.as_view(), name='participante-proj-editar'),
    url(r'^projeto/(?P<pk>[0-9]+)/participante/(?P<pkdelete>[0-9]+)/remover$', views.Projeto.as_view(), name='participante-remover'),

    url(r'^projeto/(?P<pk>[0-9]+)/anexo/upload', views.Projeto.as_view(), name='anexo-proj-upload'),
    url(r'^projeto/(?P<pk>[0-9]+)/anexo/(?P<pkdelete>[0-9]+)/remover', views.Projeto.as_view(), name='anexo-proj-remover'),

    url(r'^projeto/(?P<pk>[0-9]+)/meta/novo$', views.Projeto.as_view(), name='meta-proj-criar'),
    url(r'^projeto/(?P<pk>[0-9]+)/meta/(?P<pkmeta>[0-9]+)/editar$', views.Projeto.as_view(), name='meta-proj-editar'),
    url(r'^projeto/(?P<pk>[0-9]+)/meta/(?P<pkdelete>[0-9]+)/remover$', views.Projeto.as_view(), name='meta-proj-remover'),

    url(r'^projeto/(?P<pk>[0-9]+)/meta/(?P<pkmeta>[0-9]+)/atividade/novo$', views.Projeto.as_view(), name='atividade-meta-proj-criar'),
    url(r'^projeto/(?P<pk>[0-9]+)/meta/(?P<pkmeta>[0-9]+)/atividade/(?P<pkatividade>[0-9]+)/editar$', views.Projeto.as_view(), name='atividade-meta-proj-editar'),
    url(r'^projeto/(?P<pk>[0-9]+)/meta/(?P<pkmeta>[0-9]+)/atividade/(?P<pkdelete>[0-9]+)/remover$', views.Projeto.as_view(), name='atividade-meta-proj-remover'),

    url(r'^projeto/(?P<pk>[0-9]+)/meta/(?P<pkmeta>[0-9]+)/atividade/(?P<pkatividade>[0-9]+)/vincularparticipantes$', views.Projeto.as_view(), name='vinculo-atividade-m-proj'),

    url(r'^meta/(?P<pk>[0-9]+)/atividades_select$', views.get_atividades, name='get-atividades-select-ajax'),
    url(r'^atividade/(?P<pk>[0-9]+)/participantes_select$', views.get_atividade_bolsistas, name='get-participantes-select-ajax'),

]
