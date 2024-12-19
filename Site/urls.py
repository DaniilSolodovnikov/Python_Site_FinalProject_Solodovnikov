"""
URL configuration for Site project.

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
from App import views


urlpatterns = [
    path('', views.home, name='home'),  # Маршрут для корня сайта
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('create/', views.create_ad, name='create_ad'),
    path('success/', views.ad_success, name='ad_success'),
    path('create_ad/', views.create_ad, name='create_ad'),
    path('approve_ad/', views.approve_ad, name='approve_ad'),
]
