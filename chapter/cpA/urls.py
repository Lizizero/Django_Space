from django.urls import path, re_path
from . import views

urlpatterns = [
    path('sub/', views.useinclude),
    re_path('.*', views.Everything),
]
