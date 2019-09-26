=============
django-uniapi
=============

Django General/Universal API

Installation
============

::

    pip install django-uniapi


Urls.py
=======

::

    urlpatterns = [
        url(r'^uniapi/', include('django_uniapi.urls', namespace='django_uniapi')),
    ]


or::

    from django.conf.urls import include, url
    from django_uniapi import views as uni_views

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


Settings.py
===========

::

    INSTALLED_APPS = (
        ...
        'django_uniapi',
        ...
    )

