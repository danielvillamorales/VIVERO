from django.db import models
from webapp.models.viveros import Viveros


class Productores(models.Model):
    tipo_identificacion = models.CharField(max_length=2)
    cedula = models.CharField(max_length=20,unique=True)
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20,null=True,blank=True)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20,null=True,blank=True)
    viveros = models.ManyToManyField(Viveros)


    def __str__(self):

        return f'identificacion: {self.tipo_identificacion} , numero cedula: {self.cedula} , nombre: {self.nombre1} {self.nombre2} {self.apellido1} {self.apellido2}'


