from django.db import models
from django.utils import timezone

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos =  models.TextField()
    matricula=  models.IntegerField()
    activo =  models.BooleanField()
    created_at =  models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "alumnos"