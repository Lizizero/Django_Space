from django.shortcuts import render
from .models import userinfo
from django.http import HttpResponse


# Create your views here.
def doCheckUid(request):
    ps = userinfo.objects.filter(uid=request.GET['uid'])
    if ps.count() == 0:
        msg = 'ID可用'
    else:
        msg = 'ID已占用'
    return HttpResponse(msg, content_type="text/text;charset=utf-8")


def doAddNew(request):
    try:
        nuid = request.GET['uid']
        pwd = request.GET['pwd']
        nemail = request.GET['email']
        user = userinfo(uid=nuid, password=pwd, email=nemail)
        user.save()
        msg = '已完成注册'
        return HttpResponse(msg, content_type="text/text;charset=utf-8")
    except Exception as e:
        msg = '意外错误:%s'% e
        return HttpResponse(msg, content_type="text/text;charset=utf-8")
