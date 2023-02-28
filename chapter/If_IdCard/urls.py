from django.urls import re_path
from . import views

urlpatterns = [
    re_path('\d{18}', views.IdCard),
    re_path('.*', views.Not_Id),
]
