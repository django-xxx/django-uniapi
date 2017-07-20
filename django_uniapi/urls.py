# -*- coding: utf-8 -*-

from django.conf.urls import url

from django_uniapi import views as uni_views


urlpatterns = [
    url(r'^status$', uni_views.server_status, name='server_status'),
    url(r'^time$', uni_views.server_time, name='server_time'),
    url(r'^error$', uni_views.raise_error, name='raise_error'),
]
