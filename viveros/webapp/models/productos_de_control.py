from django.db import models
from webapp.models.tipos_productos_control import Tiposproductoscontrol

class Productoscontrol(models.Model):
    registro_ica = models.CharField(max_length=10,unique=True)
    nombre_producto = models.CharField(max_length=50)
    frecuencia_aplicacion = models.IntegerField()
    valor_producto = models.FloatField()
    tipos_productos_control = models.ForeignKey(Tiposproductoscontrol, on_delete=models.PROTECT, null=True,blank=True)

    def __str__(self):

        return f'registro ica: {self.registro_ica} , nombre del producto: {self.nombre_producto} , frecuencia de aplicacion: {self.frecuencia_aplicacion} , valor del producto: {self.valor_producto} , tipos de productos de control: {self.tipos_productos_control.__str__()} '