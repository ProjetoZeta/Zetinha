from django.conf.urls import url
from usuario import views

urlpatterns = [
    url(r'^$', views.main, name='main'),

]
