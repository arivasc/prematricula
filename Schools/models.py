from statistics import mode
from django.db import models
from django.urls import reverse
from Auth.models import *

# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=48)
    desc = models.TextField(null=True)
    estReg = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("escuelas:escuela-detail", kwargs={"pk": self.id})
    

class Malla(models.Model):
    anio = models.PositiveSmallIntegerField()
    desc = models.TextField(null=True)
    escuela = models.ForeignKey(
        Escuela,
        on_delete=models.SET_NULL,
        null=True)
    estReg = models.BooleanField(default=True)

    def __str__(self):
        return str(self.anio)

    def get_absolute_url(self):
        return reverse("mallas:malla-detail", kwargs={"pk": self.id})
    

class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    codigo = models.CharField(max_length=10, unique=True)
    semejante = models.CharField(max_length=10, null=True)
    prereq = models.CharField(max_length=64, null=True)
    desc = models.TextField(null=True)
    creditos = models.PositiveSmallIntegerField()
    malla = models.ForeignKey(
        Malla,
        on_delete=models.SET_NULL,
        null=True)
    estReg = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("cursos:curso-detail", kwargs={"pk": self.id})