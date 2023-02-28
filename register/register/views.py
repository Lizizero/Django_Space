from django.shortcuts import render


def toAddNew(request):
    return render(request, 'newuser.html')
