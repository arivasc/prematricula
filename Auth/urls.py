from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from Auth.views import UserLogin
from django.urls import path

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]