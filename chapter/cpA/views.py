from django.http import HttpResponse


def useinclude(request):
    return HttpResponse('这是应用caA的视图函数useinclude的响应')


def Everything(request):
    return HttpResponse('没有响应')
