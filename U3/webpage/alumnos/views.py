
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from alumnos.models import *
import sys
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

    alumno = None
    existe =  False
    estatus =  None
    try:
        alumno = Alumnos.objects.get(id=id)
        if(alumno.activo):
            estatus  =  "activo"
        else:
            estatus =  "De baja"
        existe = True
    except:
        existe = False
    data = {
        "alumno":alumno,
        "existe":existe,
        "id":id,
        "estatus":estatus
    }
    return render(request,"ver_alumno.html",data)

def forAlumno(request):
     return render(request,"crear_alumno.html",{})



def crearAlumno(request):
    nombre =  request.POST.get("nombre_alumno")
    apellidos =  request.POST.get("apellidos")
    matricula =  request.POST.get("matricula")
    activo =  request.POST.get("activo")
    
    estatus  = False 
    if( activo  == "1"):
        estatus =  True

    insert =  "no_creado"
    try:
        insertAlumno =  Alumnos.objects.create(
        nombre =nombre,
        apellidos= apellidos,
        matricula =  int(matricula),
        activo =  estatus
        )
        insert = "creado"
    except:
        insert = "no_creado"

    # return HttpResponse(insert)
    return render(request,"crear_alumno.html",{"crear":insert})


def updateAlumno(request):
    nombre =  request.POST.get("nombre_alumno")
    apellidos =  request.POST.get("apellidos")
    matricula =  request.POST.get("matricula")
    activo =  request.POST.get("activo")
    id =  request.POST.get("id_alumno")

    alumno =  Alumnos.objects.get(id=id)
    alumno.nombre = nombre
    alumno.apellidos = apellidos
    alumno.matricula =  matricula

    if activo == "activo":
        alumno.activo =  True
    else:
        alumno.activo = False
    updated = None
    try:
        updated = alumno.save()
        updated = True
    except:
        updated= False

    return HttpResponse(alumno)