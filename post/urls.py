from django.contrib import admin
from django.urls import path, include
from post import views

app_name='post'

urlpatterns = [
    path('new/', views.save, name='savePost'),
    path('', views.PostList.as_view(), name='all'),
    path('<username>/<int:pk>/detail/', views.PostDetail.as_view(), name='detail'),
    path('<username>/<int:pk>/edit/', views.PostUpdate.as_view(), name='edit'),
    path('<username>/<int:pk>/delete/', views.PostDelete.as_view(), name='delete'),
]
