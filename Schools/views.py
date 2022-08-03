from django.shortcuts import render
from Schools.models import Malla, Escuela, Curso

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
)

class MallaListView(ListView):
    model = Malla

class MallaDetailView(DetailView):
    model = Malla

class MallaCreateView(CreateView):
    model = Malla
    fields = [
        'anio',
        'desc',
        'escuela',
    ]

class MallaUpdateView(UpdateView):
    model = Malla
    fields = [
        'anio',
        'desc',
        'escuela',
    ]


class CursoListView(ListView):
    model = Curso

class CursoDetailView(DetailView):
    model = Curso

class CursoCreateView(CreateView):
    model = Curso
    fields = [
        'nombre',
        'codigo',
        'semejante',
        'prereq',
        'desc',
        'creditos',
        'malla',

    ]

class CursoUpdateView(UpdateView):
    model = Curso
    fields = [
        'nombre',
        'codigo',
        'semejante',
        'prereq',
        'desc',
        'creditos',
        'malla',
    ]


class EscuelaListView(ListView):
    model = Escuela

class EscuelaDetailView(DetailView):
    model = Escuela

class EscuelaCreateView(CreateView):
    model = Escuela
    fields = [
        'nombre',
        'desc',
    ]

class EscuelaUpdateView(UpdateView):
    model = Escuela
    fields = [
        'nombre',
        'desc',
    ]