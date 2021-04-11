from django.contrib import admin
from webapp.models.labores import Labores

@admin.register(Labores)
class Laboresadmin(admin.ModelAdmin):
    list_display = ('fecha_labor','descripcion_labor', 'tiposdelabores' )
    #search_fields = ('cedula','nombre1','nombre2','apellido1','apellido2')
    #list_filter = ('codigo_dane','nombre_ciudad')
    #ordering = ('id',)

    def tiposdelabores(self,objeto):
        return objeto.tipo_labores.descripcion