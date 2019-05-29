from django.contrib import admin
from django.urls import path
from certifications import views

urlpatterns = [
    path('', views.index, name='certifications_home'),
]
