from django.db import models
from django.contrib.auth.models import User #Importamos la tabla usuario que django tiene por defecto.
import os

class Departamento(models.Model):
    nombre= models.TextField(max_length=30, blank=False)
    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.TextField(max_length=30, blank=False)
    def __str__(self):
        return self.nombre

class TipoDeDocumento(models.Model):
    nombre = models.TextField(blank=False)
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.TextField(blank=False)
    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    tipo_documento_id = models.ForeignKey(TipoDeDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=20 ,blank=False)
    nombre1 = models.CharField(max_length=20 ,blank=False)
    nombre2 = models.CharField(max_length=20 ,blank=True)
    apellido1 = models.CharField(max_length=20 ,blank=False)
    apellido2 = models.CharField(max_length=20 ,blank=False)
    genero_id = models.ForeignKey(Genero, on_delete=models.CASCADE)
    departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio_id = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre1+" - "+self.numero_documento



