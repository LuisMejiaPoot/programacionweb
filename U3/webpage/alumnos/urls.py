from django.urls import path 
from . import views

urlpatterns = [
    path('listado/<int:id>',views.index,name="index"),
    path("listadoAlumnos",views.alumnos,name="listado_alumnos"),
    path("ver_alumno/<int:id>",views.ver_alumno, name="ver_alumno")

]