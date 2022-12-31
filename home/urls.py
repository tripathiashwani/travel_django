from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("water", views.water, name='water'), 
    path("desert", views.desert, name='desert'), 
    path("forest", views.forest, name='forest'), 
    path("monuments", views.monuments, name='monuments'), 
    path("search", views.search, name='search'), 
]