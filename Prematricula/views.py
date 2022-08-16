from django.shortcuts import render
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'ta/home.html')

def about(request):
    return render(request, 'ta/about.html', {'title':'Acerca de la Escuela'})

def malla(request):
    return render(request, 'ta/malla.html', {'title':'Malla Curricular 2017'})

def login(request):
    return render(request, 'ta/login.html', {'title':'Inicio de Sesión'})

def aboutus(request):
    return render(request, 'ta/aboutus.html', {'title':'Acerca de Nosotros'})