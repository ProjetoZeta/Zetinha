from django.conf.urls import url
from administracao import views

urlpatterns = [
    url(r'^$', views.main, name='Página Principal'),
    url(r'^usuario$', views.user, name='Manter Usuário'),
    url(r'^cargo', views.cargo, name='cargo'),
    url(r'^entidade', views.entidade, name='entidade')
]
