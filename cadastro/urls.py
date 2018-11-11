from django.conf.urls import url
from django.urls import include, path
from . import views
# from administracao.views import Pdf

urlpatterns = [
    
    url(r'^cargo$', views.Cargo.as_view(), name='cargo'),
    url(r'^cargo/(?P<pk>[0-9]+)/editar$', views.Cargo.as_view(), name='cargo-editar'),
    url(r'^cargo/(?P<pkdelete>[0-9]+)/remover$', views.Cargo.as_view(), name='cargo-remover'),

    url(r'^entidade$', views.Entidade.as_view(), name='entidade'),
    url(r'^entidade/(?P<pk>[0-9]+)/editar$', views.Entidade.as_view(), name='entidade-editar'),
    url(r'^entidade/(?P<pkdelete>[0-9]+)/remover$', views.Entidade.as_view(), name='entidade-remover'),

    url(r'^funcao$', views.Funcao.as_view(), name='funcao'),
    url(r'^funcao/(?P<pk>[0-9]+)/editar$', views.Funcao.as_view(), name='funcao-editar'),
    url(r'^funcao/(?P<pkdelete>[0-9]+)/remover$', views.Funcao.as_view(), name='funcao-remover'),

    url(r'^responsavel$', views.Responsavel.as_view(), name='responsavel'),
    url(r'^responsavel/(?P<pk>[0-9]+)/editar$', views.Responsavel.as_view(), name='responsavel-editar'),
    url(r'^responsavel/(?P<pkdelete>[0-9]+)/remover$', views.Responsavel.as_view(), name='responsavel-remover'),

    url(r'^usuario$', views.Usuario.as_view(), name='usuario'),
    url(r'^usuario/(?P<pk>[0-9]+)/editar$', views.Usuario.as_view(), name='usuario-editar'),
    url(r'^usuario/(?P<pkdelete>[0-9]+)/remover$', views.Usuario.as_view(), name='usuario-remover'),

    url(r'^bolsista$', views.BolsistaList.as_view(), name='bolsista'),
    url(r'^bolsista/novo$', views.Bolsista.as_view(), name='bolsista-criar'),
    url(r'^bolsista/(?P<pk>[0-9]+)/editar$', views.Bolsista.as_view(), name='bolsista-editar'),
    url(r'^bolsista/(?P<pkdelete>[0-9]+)/remover$', views.Bolsista.as_view(), name='bolsista-remover'),

    url(r'^bolsista/arquivo_upload$', views.BolsistaDocumento.as_view(), name='upload-arquivo-bolsista'),
    url(r'^bolsista/arquivo/(?P<pkdelete>[0-9]+)/remover$', views.BolsistaDocumento.as_view(), name='remover-arquivo-bolsista'),

    url(r'^bolsista/emprestimoequipamento$', views.BolsistaEmprestimoEquipamento.as_view(), name='emprestimo-equipamento-bolsista'),
    url(r'^bolsista/emprestimoequipamento/(?P<pkdelete>[0-9]+)/remover$', views.BolsistaEmprestimoEquipamento.as_view(), name='remover-emprestimo-equipamento-bolsista'),

    url(r'documento/(?P<pk>[0-9]+)', views.Documento.as_view(), name='show-document'),

    url(r'emprestimo/(?P<pk>[0-9]+)', views.EmprestimoEquipamento.as_view(), name='show-emprestimoequipamento'),

    url(r'^projeto$', views.ProjetoList.as_view(), name='projeto'),
    url(r'^projeto/novo$', views.Projeto.as_view(), name='projeto-criar'),
    url(r'^projeto/(?P<pk>[0-9]+)/editar$', views.Projeto.as_view(), name='projeto-editar'),
    url(r'^projeto/(?P<pkdelete>[0-9]+)/remover$', views.Projeto.as_view(), name='projeto-remover'),

    url(r'^projeto/(?P<pk>[0-9]+)/participante/novo$', views.ParticipanteProjeto.as_view(), name='participante-proj-criar'),
    url(r'^projeto/(?P<pk>[0-9]+)/participante/(?P<pkparticipante>[0-9]+)/editar$', views.ParticipanteProjeto.as_view(), name='participante-proj-editar'),

    url(r'^projeto/(?P<pk>[0-9]+)/participante/(?P<pkdelete>[0-9]+)/remover$', views.ParticipanteProjeto.as_view(), name='participante-remover'),

    url(r'projeto/(?P<pk>[0-9]+)/anexo/upload', views.AnexoProjeto.as_view(), name='anexo-proj-upload'),
    url(r'projeto/anexo/(?P<pkdelete>[0-9]+)/remover', views.AnexoProjeto.as_view(), name='anexo-proj-remover'),

    url(r'anexo/(?P<pk>[0-9]+)', views.Anexo.as_view(), name='show-anexo'),


]
