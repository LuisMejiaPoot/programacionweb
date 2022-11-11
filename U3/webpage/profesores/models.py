from django.db import models
from django.conf import settings
from django.utils import timezone
from blog import models as blogs

# Create your models here.

class Profesores(models.Model):

    nombre = models.CharField(max_length=100)
    apellidos =  models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey(blogs.Blog, on_delete= models.CASCADE)

    class Meta:
        db_table ="Profesores"
