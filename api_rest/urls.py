from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:nickname>/', views.get_user_by_nickname, name='get_user_by_nickname'),
]
