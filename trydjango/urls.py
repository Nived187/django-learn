"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view,pic_view,first_view
from learning.views import view1,phone_create_view,project_view
from products.views import input_values
from abhilasha.views import complain_register
from one.views import showroom_view

urlpatterns = [
    path("",first_view),
    path("admin/", admin.site.urls),
    path('home/',home_view,name='home'),
    path('pic/',pic_view),

    path("learn/",view1),
    path("create/",phone_create_view),
     path("project/",project_view),
     path("input/",input_values),
     path("abhilasha/",complain_register),
     path("main/",showroom_view)


]
