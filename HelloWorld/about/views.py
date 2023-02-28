from django.http import HttpResponse
from django.urls import reverse


def about(request):
    s = "HelloWorld项目是在本书第一章实践环节中创建的一个Django项目！<br/>创建时间：2022-10-3。<br/>" + \
        "<a href='" + reverse("hello") + "'>" + "返回首页<a/>"
    return HttpResponse(s)
