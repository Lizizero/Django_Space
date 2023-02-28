from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = {
    re_path(r'^[A-Za-z]+$', views.CharURL),
    re_path(r'^\d{2,}$', views.NumberURL),
    path('test/<urlData>/', views.getData),
    path('cpA/', include('cpA.urls')),
    path('IdCard/', include('If_IdCard.urls')),
    path("admin/", admin.site.urls),
}
