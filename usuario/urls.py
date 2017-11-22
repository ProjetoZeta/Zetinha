from django.conf.urls import url
from administracao import views

urlpatterns = [
    url(r'^$', views.main, name='main'),

]
