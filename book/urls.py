from django.contrib import admin
from django.urls import path, include
from book import views

app_name='book'

urlpatterns = [
    path('', views.search, name='api_search'),
]
