from django.contrib import admin
from webapp.models.productores import Productores

@admin.register(Productores)
class Productoresadmin(admin.ModelAdmin):
    list_display = ('tipo_identificacion','cedula', 'nombrecompleto', )
    search_fields = ('cedula','nombre1','nombre2','apellido1','apellido2')
    #list_filter = ('codigo_dane','nombre_ciudad')
    ordering = ('id',)

    def nombrecompleto(self,objeto):
        texto = ''
        if objeto.nombre2 == None:
            if objeto.apellido2 == None:
                texto = f'{objeto.nombre1} {objeto.apellido1}'
            else:
                texto= f'{objeto.nombre1} {objeto.apellido1} {objeto.apellido2}'
        else:
            texto = f'{objeto.nombre1} {objeto.nombre2} {objeto.apellido1} {objeto.apellido2}'
        return f'{texto}'
