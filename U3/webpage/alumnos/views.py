
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from alumnos.models import *

def index(request,id):
    diccionary = {
        "alumno":{
            "nombre":"Carlos",
            "grupo":"A",
            "grado": 1
        },
        "blogs": id
    }
    # data =  Blog(nombre="Blog 100",description ='Blog description 1', capacidad = 15 )
    # data.save()

    return JsonResponse(diccionary)
    # return HttpResponse("Hola Django")
    # return  HttpResponse("Hola a todos")
    # return render(request,"index.html")

def alumnos(request):
    edad =  17
    localidad =  "Mérida"

    alumnos = [
        {
            "nombre":"Carlos",
            "apellidos":"Perez",
            "carrera":"Desarrollo de software",
            "semestre": 5
        },
        {
            "nombre":"Maria",
            "apellidos":"Lopez",
            "carrera":"Derecho",
            "semestre": 2
        },
        {
            "nombre":"Damian",
            "apellidos":"Carrillo",
            "carrera":"Derecho",
            "semestre": 2
        },
    ]
    # data =Blog.objects.filter(capacidad__gte=15)
    alumnosDB  =  Alumnos.objects.all()
    datos = {
        "nombre":"Luis Mejia",
        "edad":edad,
        "localidad":localidad,
        "alumnos":alumnos,
        "alumnosDB": alumnosDB  
    }

    return render(request,"listado.html",datos)



def ver_alumno(request, id):
    
    return render(request,"ver_alumno.html",{})
