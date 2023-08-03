"""
URL configuration for project25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('fbv/',fbv,name='fbv'),
    path('cbv/',cbv.as_view(),name='cbv'),
    path('cbv_first/',cbv_first.as_view(),name='cbv_first'),
    path('cbv_sec/',cbv_sec.as_view(),name='cbv_sec'),



    path('insert_cbv/',insert_cbv.as_view(),name='insert_cbv'),

    path('bhavya/',TemplateView.as_view(template_name='bhavya.html'),name='bhavya')
]
