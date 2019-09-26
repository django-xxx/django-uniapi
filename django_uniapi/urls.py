# -*- coding: utf-8 -*-

from django.conf.urls import url
from django_uniapi import views as uni_views


app_name = 'django_uniapi'


urlpatterns = [
    url(r'^status$', uni_views.server_status, name='server_status'),
    url(r'^time$', uni_views.server_time, name='server_time'),
    url(r'^error$', uni_views.raise_error, name='raise_error'),
]

urlpatterns += [
    url(r'^set_cookie$', uni_views.set_cookie, name='set_cookie'),
    url(r'^del_cookie$', uni_views.del_cookie, name='del_cookie'),
    url(r'^del_cookie2$', uni_views.del_cookie2, name='del_cookie2'),
]
