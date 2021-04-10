from django.db import models
from webapp.models.ciudades import Ciudades

class Viveros(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=20)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.SET_NULL, null=True)

    def __str__(self):

        return f'codigo viveros: {self.codigo}, nombre vivero: {self, nombre}, ciudad vivero: {self.ciudad.__str__()}'



