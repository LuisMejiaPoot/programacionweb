
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    diccionary = {
        "alumno":{
            "nombre":"Carlos",
            "grupo":"A",
            "grado": 1
        }
    }
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
    
    datos = {
        "nombre":"Luis Mejia",
        "edad":edad,
        "localidad":localidad,
        "alumnos":alumnos
    }
    return render(request,"listado.html",datos)
