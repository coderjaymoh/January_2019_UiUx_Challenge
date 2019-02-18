from django.contrib import admin
from django.urls import path
from . import views
from .views import register, verifyUser

urlpatterns = [
    path('', views.register, name='register'),
    path('validation/', views.verifyUser, name='verifyUser'),
]
