from django.conf.urls import include, url
from accounts.views import register as register
from django.contrib.auth.views import login as login
from django.contrib.auth.views import logout as logout


urlpatterns = [
    url(r'^sign-in', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout$', logout, {'next_page': 'core:index'}, name='logout'),
    url(r'^sign-up$', register, name='register'),
]