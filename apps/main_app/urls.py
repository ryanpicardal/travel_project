
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^home$', views.home),
    url(r'^addtrip$', views.addtrip),
    url(r'^createtrip$', views.createtrip),
    url(r'^destination/(?P<id>\d+)$', views.destination),
]
