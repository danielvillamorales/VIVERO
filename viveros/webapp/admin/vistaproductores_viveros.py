from django.contrib import admin
from webapp.models.productores_viveros import Productores_viveros

@admin.register(Productores_viveros)
class Productores_viverosadmin(admin.ModelAdmin):
    list_display = ('productores','viveros')
    search_fields = ('productores__nombre1','productores__nombre2','productores__apellido1','productores__apellido2','productores__cedula')
    #list_editable = ('descripcion',)
    list_filter = ('productores',)
    ordering = ('id',)

