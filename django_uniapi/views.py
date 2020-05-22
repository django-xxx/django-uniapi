# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django_response import response
from TimeConvert import TimeConvert as tc


def server_status(request):
    return response()


def server_time(request):
    ms = ('ms' in request.GET) or ('ms' in request.POST)
    return response(data={
        'time': tc.utc_datetime(ms=ms)
    })


def raise_error(request):
    # Raise ZeroDivisionError
    zero_division_error = 1 / 0
    return response()


@staff_member_required
def set_cookie(request):
    cookie_key = request.GET.get('k', '')
    cookie_value = request.GET.get('v', '')

    signed_cookie = bool(int(request.GET.get('s', 1)))

    cookie_domain = bool(int(request.GET.get('d', 1)))
    if hasattr(settings, 'DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC') and hasattr(settings.DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC, '__call__'):
        cookie_domain = settings.DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC(request)

    max_age = hasattr(settings, 'DJANGO_WE_COOKIE_MAX_AGE') and getattr(settings, 'DJANGO_WE_COOKIE_MAX_AGE') or 30 * 24 * 60 * 60  # 30d
    cookie_salt = hasattr(settings, 'DJANGO_WE_COOKIE_SALT') and getattr(settings, 'DJANGO_WE_COOKIE_SALT') or 'djwe'  # Salt for ``set_signed_cookie``

    resp = response()

    if signed_cookie:
        resp.set_signed_cookie(cookie_key, cookie_value, domain=cookie_domain, salt=cookie_salt, **{
            'max_age': max_age,
            'httponly': True,
        })
    else:
        resp.set_cookie(cookie_key, cookie_value, domain=cookie_domain, max_age=max_age)

    return resp


@staff_member_required
def del_cookie(request):
    cookie_key = request.GET.get('k', '')

    cookie_domain = bool(int(request.GET.get('d', 1)))
    if hasattr(settings, 'DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC') and hasattr(settings.DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC, '__call__'):
        cookie_domain = settings.DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC(request)

    resp = response()

    resp.delete_cookie(cookie_key, domain=cookie_domain)

    return resp


def del_cookie2(request):
    cookie_key = request.GET.get('k', '')

    cookie_domain = bool(int(request.GET.get('d', 1)))
    if hasattr(settings, 'DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC') and hasattr(settings.DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC, '__call__'):
        cookie_domain = settings.DJANGO_UNIAPI_COOKIE_DOMAIN_FUNC(request)

    resp = response()

    if hasattr(settings, 'DJANGO_UNIAPI_STAFF_MEMBER_REQUIRED') and not getattr(settings, 'DJANGO_UNIAPI_STAFF_MEMBER_REQUIRED'):
        resp.delete_cookie(cookie_key, domain=cookie_domain)

    return resp
