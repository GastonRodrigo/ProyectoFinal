from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)

class empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellida = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)

class proveedores(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)

class productos(models.Model):
    modelo = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    medidas = models.CharField(max_length=30)
