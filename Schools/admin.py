from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Escuela)
admin.site.register(Malla)
admin.site.register(Curso)