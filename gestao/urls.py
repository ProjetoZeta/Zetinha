from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.WebLoader.main, name='Página Principal'),
    url(r'^usuario$', views.WebLoader.user, name='Manter Usuário')
]
