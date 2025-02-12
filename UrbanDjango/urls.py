"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import GetFunc, get_class
# from task3.views import PlatformTemplate, CartTemplate, CosmeticsTemplate
from task4.views import PlatformTemplate, CartTemplate, CosmeticsTemplate
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', get_class),
    path('func/', GetFunc.as_view()),
    path('platform/', PlatformTemplate.as_view()),
    path('platform/cart', CartTemplate.as_view()),
    path('platform/cosmetics/', CosmeticsTemplate.as_view()),
    path('sign_up_by_django', sign_up_by_django),
    path('sign_up_by_html', sign_up_by_html),
]
