from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model):
    nombre =  models.CharField(max_length=100),
    description  =  models.TextField(default="Description")
    capacidad =  models.IntegerField(default=20)
    tipo =  models.CharField(max_length=10,default =  "A")
    created_date =  models.DateTimeField(default=timezone.now)


    # def clave(self):
    #     return f"{self.nombre}-Uni"
    
    class Meta:
        ordering = ["created_date"]
        db_table = 'blog'




