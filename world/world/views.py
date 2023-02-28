from django.http import HttpResponse


def hello(requset):
    return HttpResponse("Hello World everyone!")
