from django.db import models


class Tiposproductoscontrol(models.Model):
    tipo_producto = models.CharField(max_length=30)
    periodo_carencia = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha_ua = models.DateTimeField()


    def __str__(self):

        return f'tipo de producto: {self.tipo_producto} , periodo de carencia: {self.periodo_carencia} , nombre: {self.nombre} , fecha de ultima aplicacion: {self.fecha_ua}'