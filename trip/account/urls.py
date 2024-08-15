from django.contrib import admin
from django.urls import path
from account import views



urlpatterns = [
     path("login",views.LoginView.as_view(),name='login'),
     path("register",views.RegisterView.as_view(),name='register'),
  
]













 