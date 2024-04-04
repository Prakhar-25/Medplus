from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("about", views.about, name = "about"),
    path("service", views.service, name = "service"),
    path("appointment", views.appointment, name = "appointment"),
    path("contact", views.contact, name = "contact"),
    path("team", views.team, name = "team")
]
