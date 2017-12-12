from django.conf.urls import url
from administracao import views

urlpatterns = [
    url(r'^$', views.main, name='main'),

    url(r'^cargo$', views.cargo, name='cargo'),
    url(r'^cargo/(?P<pk>[0-9]+)/editar$', views.cargo, name='cargo-editar'),
    url(r'^cargo/(?P<pkdelete>[0-9]+)/remover$', views.cargo, name='cargo-remover'),

    url(r'^entidade$', views.entidade, name='entidade'),
    url(r'^entidade/(?P<pk>[0-9]+)/editar$', views.entidade, name='entidade-editar'),
    url(r'^entidade/(?P<pkdelete>[0-9]+)/remover$', views.entidade, name='entidade-remover'),

    url(r'^funcao$', views.funcao, name='funcao'),
    url(r'^funcao/(?P<pk>[0-9]+)/editar$', views.funcao, name='funcao-editar'),
    url(r'^funcao/(?P<pkdelete>[0-9]+)/remover$', views.funcao, name='funcao-remover'),

    url(r'^responsavel$', views.responsavel, name='responsavel'),
    url(r'^responsavel/(?P<pk>[0-9]+)/editar$', views.responsavel, name='responsavel-editar'),
    url(r'^responsavel/(?P<pkdelete>[0-9]+)/remover$', views.responsavel, name='responsavel-remover'),

    url(r'^usuario$', views.usuario, name='usuario'),
    url(r'^usuario/(?P<pk>[0-9]+)/editar$', views.usuario, name='usuario-editar'),
    url(r'^usuario/(?P<pkdelete>[0-9]+)/remover$', views.usuario, name='usuario-remover'),

    url(r'^bolsista$', views.bolsista, name='bolsista'),
    url(r'^bolsista/novo$', views.bolsista_handle, name='bolsista-criar'),
    url(r'^bolsista/(?P<pk>[0-9]+)/editar$', views.bolsista_handle, name='bolsista-editar'),
    url(r'^bolsista/(?P<pkdelete>[0-9]+)/remover$', views.bolsista, name='bolsista-remover'),

    url(r'^bolsista/arquivo_upload$', views.handle_arquivo_bolsista, name='upload-arquivo-bolsista'),
    url(r'^bolsista/arquivo/(?P<pkdelete>[0-9]+)/remover$', views.handle_arquivo_bolsista, name='remover-arquivo-bolsista'),


]
