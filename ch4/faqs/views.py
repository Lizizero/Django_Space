from .models import faqsdata
from django.http import HttpResponse


def info(request, data):
    ds = faqsdata.objects.filter(sex=data)
    s = ""
    for d in ds:
        s += str(d.id) + "  " + d.name + "  " + d.sex + "  " + str(d.age) + "<br>"
    return HttpResponse(s)

# Create your views here.
