from django.conf.urls import url
from gestao import views

urlpatterns = [
    url(r'^$', views.main, name='Página Principal'),
    url(r'^usuario$', views.user, name='Manter Usuário')
]
