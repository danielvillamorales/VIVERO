from django.db import models


class Tiposlabores(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f'tipos de labores: {self.descripcion}'