from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_all_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<str:nickname>/', views.get_user_by_nickname, name='get_user_by_nickname'),
    path('users/<str:nickname>/update/', views.update_user, name='update_user'),
]
