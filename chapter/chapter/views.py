from django.http import HttpResponse


def CharURL(request):
    return HttpResponse("你输入的URL中只包含大小字母")


def NumberURL(request):
    return HttpResponse('你输入的URL中只包含数字')


def getData(request, urlData):
    return HttpResponse('从URL获取的数据：', +urlData)
