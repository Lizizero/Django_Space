from django.http import HttpResponse


def IdCard(request):
    return HttpResponse('这是身份号码')
def Not_Id(request):
    return HttpResponse('乱了乱了哈哈哈')
