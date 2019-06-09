from django.contrib import admin
from django.urls import path
from tutorials import views

urlpatterns = [
    path('', views.index, name='tutorials_home'),
    path('python', views.python_home, name='python_home'),
]
