from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from Auth.views import UserLogin
from Auth.views import register_from_csv, register_cursos_csv
from django.urls import path

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('csv-alumnos/', register_from_csv, name= 'csv-alumnos'),
    path('csv-cursos/', register_cursos_csv, name= 'csv-cursos'),
]