from django.shortcuts import render

# Create your views here.
from .models import sysuser
from django.http import HttpResponse


def user(request):
    ds = sysuser.objects.all()
    print(ds)
    s = ''
    for a in ds:
        s += str(a.id) + ' ' + a.username + "<br>"
    return HttpResponse(s)
