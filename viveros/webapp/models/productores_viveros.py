from django.db import models
from webapp.models.productores import Productores
from webapp.models.viveros import Viveros

class Productores_viveros(models.Model):
    productores = models.ForeignKey(Productores, on_delete=models.SET_NULL, null=True)
    viveros = models.ForeignKey(Viveros, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'productores: {self.productores.__str__()}, vivero: {self.viveros.__str__()}'