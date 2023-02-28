from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def getUrlNoPara(request):
    return HttpResponse("请求的URL路径为：%s" % reverse('urlNoPara'))


def getUrlArgs(request, data):
    return HttpResponse("请求的URL路径为：%s" % reverse('UrlArgs', args=['abcd']))


def getUrlKwargs(request, data):
    return HttpResponse("请求的URL路径为：%s" % reverse('UrlKwargs', kwargs={'data': 1234}))


def getViewUrl(request):
    return HttpResponse("请求的URL路径为：%s" %
                        reverse(getUrlKwargs, kwargs={'data': 1234}))


def reverseInTemplates(request, data):
    return render(request, 'showurl.html', {'data': data})
