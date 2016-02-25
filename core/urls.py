from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/request$', views.new_request, name='new_request'),
    url(r'^new/client$', views.new_client, name='new_client')
]