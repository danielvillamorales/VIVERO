from django.db import models
from webapp.models.tipos_de_labores import Tiposlabores
from webapp.models.productos_de_control import Productoscontrol

class Labores(models.Model):
    fecha_labor = models.DateTimeField()
    descripcion_labor = models.CharField(max_length=255)
    tipo_labores = models.ForeignKey(Tiposlabores, on_delete=models.PROTECT, null=True)
    productos_control = models.ForeignKey(Productoscontrol, on_delete=models.PROTECT, null=True)


    def __str__(self):

        return f'fecha labor: {self.fecha_labor} , descripcion labor: {self.descripcion_labor} , tipos de labores: {self.tipo_labores_labor.__str__()} , productos de control: {self.productos_control.__str__()}'
