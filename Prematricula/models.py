from django.db import models
from Auth.models import User
from Schools.models import Escuela, Curso

# Create your models here.
class PrematriCab(models.Model):
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
    estReg = models.BooleanField(default=True)