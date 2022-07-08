from statistics import mode
from django.db import models
from Auth.models import *

# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=48)
    desc = models.TextField(null=True)
    estReg = models.BooleanField(default=True)
    

class Malla(models.Model):
    anio = models.PositiveSmallIntegerField()
    desc = models.TextField(null=True)
    escuela = models.ForeignKey(
        Escuela,
        on_delete=models.SET_NULL,
        null=True)
    estReg = models.BooleanField(default=True)

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

'''class PrematriCab(models.Model):
    nombre = models.CharField(max_length=60, null=True)
    desc = models.TextField(null=True)
    escuela = models.ForeignKey(
        Escuela,
        on_delete=models.SET_NULL,
        null=True)
    estReg = models.BooleanField(default=True)

class PrematriCurso(models.Model):
    prematriCab = models.ForeignKey(
        PrematriCab,
        on_delete=models.SET_NULL,
        null=True)
    curso = models.ForeignKey(
        Curso,
        on_delete=models.SET_NULL,
        null=True)
    estReg = models.BooleanField(default=True)

class DetallePrematriCurso(models.Model):
    prematriCurso = models.ForeignKey(
        PrematriCurso,
        on_delete=models.SET_NULL,
        null=True)
    alumno = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True)
    estReg = models.BooleanField(default=True)'''