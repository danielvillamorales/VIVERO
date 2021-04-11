from django.contrib import admin
from webapp.models.productos_de_control import Productoscontrol

@admin.register(Productoscontrol)
class Productoscontroladmin(admin.ModelAdmin):
    list_display = ('registro_ica','nombre_producto', 'frecuencia_aplicacion','valor_producto','tipo' )
    #search_fields = ('cedula','nombre1','nombre2','apellido1','apellido2')
    #list_filter = ('codigo_dane','nombre_ciudad')
    #ordering = ('id',)

    def tipo(self,objeto):
        return objeto.tipos_productos_control.tipo_producto