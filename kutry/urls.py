"""
URL configuration for kutry project.

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
from django.contrib import admin
from django.urls import path, include
from appu.views import about, index, welcome, propertyType, propertyList, propertyAgent, \
    testimonials, contact  # Import your home view

from django.urls import path


urlpatterns = [
    path('', index, name='index'),  # Root URL
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('property-agent/', propertyAgent, name='property-agent'),
    path('property-list/', propertyList, name='property-list'),
    path('property-type/', propertyType, name='property-type'),
    path('testimonial/', testimonials, name='testimonial'),
    path('welcome/', welcome, name='welcome'),
]




