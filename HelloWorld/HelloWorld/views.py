from django.http import HttpResponse
from django.urls import reverse


def hello(request):
    ht = "Hello World! <br/>导航列表：<br>" + \
         "<a href='" + reverse("about") + "'>" + "关于HelloWorld</a>"
    return HttpResponse(ht)
