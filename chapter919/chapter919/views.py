from django.http import HttpResponse
from html import escape


def getData(request, urlData):
    return HttpResponse('从URL获取的数据:' + urlData)


def getData1(request, data):
    s = "使用str转换器，数据为%s，类型为%s" % (data, type(data))
    return HttpResponse(escape(s))


def getData2(request, data):
    s = "使用int转换器，数据为%s，类型为%s" % (data, type(data))
    return HttpResponse(escape(s))


def getNumber(request, data, ex):
    return HttpResponse("从URL中获取数据为%s，附加数据为%s" % (data, ex))


def getName(request, name, identity):
    return HttpResponse("从URL中获取人名是：%s，身份为%s" % (name, identity))


def useDefault(request, data=123):
    return HttpResponse("使用默认值参数data=123,当前值：%s" % data)
