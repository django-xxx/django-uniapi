# -*- coding: utf-8 -*-

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
