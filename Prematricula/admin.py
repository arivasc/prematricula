from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PrematriCab)
admin.site.register(PrematriCurso)
admin.site.register(DetallePrematriCurso)