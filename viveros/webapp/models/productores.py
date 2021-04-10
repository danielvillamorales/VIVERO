from django.db import models

class Productores(models.Model):
    tipo_identificacion = models.CharField(max_length=2)
    cedula = models.CharField(max_length=20)
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)

    def __str__(self):

        return f'identificacion: {self.tipo_identificacion} , numero cedula: {self.cedula} , nombre: {self.nombre1} {self.nombre2} {self.apellido1} {self.apellido2}'


