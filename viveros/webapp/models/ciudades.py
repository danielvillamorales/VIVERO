from django.db import models


class Ciudades(models.Model):
    codigo_dane = models.CharField(max_length=6,unique=True)
    nombre_ciudad = models.CharField(max_length=255)

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return f'codigo dane: {self.codigo_dane} , nombre: {self.nombre_ciudad}'


