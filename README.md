# django-uniapi
Django General/Universal API

## Installation
```shell
pip install django-uniapi
```

## Urls.py
```python
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^uniapi/', include('django_uniapi.urls', namespace='django_uniapi')),
]
```
or
```python
from django.urls import re_path
from django_uniapi import views as uni_views

urlpatterns = [
    re_path(r'^status$', uni_views.server_status, name='server_status'),
    re_path(r'^time$', uni_views.server_time, name='server_time'),
    re_path(r'^error$', uni_views.raise_error, name='raise_error'),
]

urlpatterns += [
    re_path(r'^set_cookie$', uni_views.set_cookie, name='set_cookie'),
    re_path(r'^del_cookie$', uni_views.del_cookie, name='del_cookie'),
    re_path(r'^del_cookie2$', uni_views.del_cookie2, name='del_cookie2'),
]
```

## Settings.py
```python
INSTALLED_APPS = (
    ...
    'django_uniapi',
    ...
)
```
