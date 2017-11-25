from django.conf.urls import url
from bolsista import views

urlpatterns = [
    url(r'^$', views.main, name='main')
]
