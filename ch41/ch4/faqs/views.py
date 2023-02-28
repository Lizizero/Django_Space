from .models import faqsdata
from django.http import HttpResponse

def info(request,data):
    ds=faqsdata.objects.filter(sex=data)#筛选出指定性别的记录存放到ds
    s=""
    #遍历ds，得到html字符串
    for d  in ds:
        s+=str(d.id)+"  "+d.name+"  "+d.sex+"  "+str(d.age)+"<br>"
    return HttpResponse(s)