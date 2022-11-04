from django.urls import path 
from . import views

urlpatterns = [
    path('listado',views.index,name="index"),
    path("listadoAlumnos",views.alumnos,name="listado_alumnos"),

]