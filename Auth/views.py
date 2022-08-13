from django.shortcuts import render

from django.http import JsonResponse
from csv import reader
from Auth.models import User
from Schools.models import Escuela

from django.contrib.auth.views import LoginView    

class UserLogin(LoginView):
    template_name = 'LoginView_form.html'

def register_from_csv(request):
    with open('templates/csv/test-ips.csv', encoding="utf8") as csv_file:
        csvf = reader(csv_file)
        #_ = next(csvf)
        for row in csvf:
            alumno = User()
            alumno.email = row[7]
            alumno.cui = row[1]
            alumno.dni = row[3]
            alumno.last_name = row[4] + " " + row[5]
            alumno.name = row[6]
            escuela = Escuela.objects.get(nombre=row[9])
            alumno.escuela = escuela
            alumno.set_password(row[1])
            alumno.save()
    
    return JsonResponse('Creación de alumnos desde csv trabajando...', safe= False)
