from django.contrib import admin
from django.urls import path, include
from post import views

app_name='post'

urlpatterns = [
    path('new/', views.save, name='savePost'),
    path('', views.PostList.as_view(), name='all'),
    path('edit/', views.save, name='editPost'),
]
