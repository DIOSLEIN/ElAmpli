from django.db import models
from django.utils import timezone

# Create your models here.


class Usuario(models.Model):
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    appat = models.CharField(max_length=50)#appat= apellido paterno
    apmat = models.CharField(max_length=50)#apmat= apellido materno
    fecha_nacimiento = models.DateField()
    #selecion de region y comuna
    email = models.CharField(max_length=50)
    #contrasenia

    def __str__(self):
        return self.nombre
        
