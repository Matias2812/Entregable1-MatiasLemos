
from django.db import models


# Create your models here.


class Auto(models.Model):
    
    marca = models.CharField(max_length=40)

    ruedas = models.IntegerField()

    creacion = models.IntegerField()



class Oficinas(models.Model):

    tipos = models.CharField(max_length=40)

    cantidad = models.IntegerField()



class Perros(models.Model):

    raza = models.CharField(max_length=40)

    edad = models.IntegerField()