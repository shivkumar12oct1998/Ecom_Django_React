from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getroutes/',views.getroutes),
    path('getproducts/',views.getproduct),
     path('getproduct/<str:pk>',views.getproducts),
     
]