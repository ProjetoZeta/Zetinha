from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.felipe, name='felipe'),
    url(r'^usuario$', views.fuck, name='fuck')
]