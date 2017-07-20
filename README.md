# django-uniapi
Django General/Universal API

## Installation
```shell
pip install django-uniapi
```

## Urls.py
```python
urlpatterns = [
    url(r'^uniapi/', include('django_uniapi.urls', namespace='uniapi')),
]
```
or
```python
from django.conf.urls import include, url
from django_uniapi import views as uni_views

urlpatterns = [
    url(r'^status$', uni_views.server_status, name='server_status'),
    url(r'^time$', uni_views.server_time, name='server_time'),
    url(r'^error$', uni_views.raise_error, name='raise_error'),
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
