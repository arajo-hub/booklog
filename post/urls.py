from django.contrib import admin
from django.urls import path, include
from post import views

app_name='post'

urlpatterns = [
    path('', views.save, name='savePost'),
]
