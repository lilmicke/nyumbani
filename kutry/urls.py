from django.contrib import admin
from django.urls import path
from appu import views

from appu.views import (
    about, index, welcome, propertyType, propertyList, propertyAgent,
    testimonials, contact, login_view, add_property, signup, apartments,
    building, garage, home, office, townhouse, villas, shop
)

urlpatterns = [
    path('', index, name='index'),  # Root URL
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('property-agent/', propertyAgent, name='property-agent'),
    path('property-list/', propertyList, name='property-list'),
    path('property-type/', propertyType, name='property-type'),
    path('testimonial/', testimonials, name='testimonial'),
    path('welcome/', welcome, name='welcome'),
    path('login/', login_view, name='login'),
    path('add_property/', add_property, name='add_property'),
    path('signup/', signup, name='signup'),
    path('apartments/', apartments, name='apartments'),
    path('building/', building, name='building'),
    path('garage/', garage, name='garage'),
    path('home/', home, name='home'),
    path('office/', office, name='office'),
    path('townhouse/', townhouse, name='townhouse'),
    path('villas/', villas, name='villas'),
    path('shop/', shop, name='shop'),
]
