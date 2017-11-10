from django.conf.urls import url
from administracao import views

urlpatterns = [
    url(r'^$', views.main, name='Página Principal'),
    url(r'^cargo$', views.cargo, name='cargo'),
    url(r'^cargo/(?P<pk>[0-9]+)/remover$', views.CargoDelete.as_view(), name='cargo-remover'),

    url(r'^entidade$', views.entidade, name='entidade'),
    url(r'^funcao$', views.funcao, name='funcao'),
    url(r'^responsavel$', views.responsavel, name='responsavel'),
    url(r'^usuario$', views.usuario, name='usuario')
]
