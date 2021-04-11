from django.contrib import admin
from webapp.models.viveros import Viveros

@admin.register(Viveros)
class Viverosadmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre','ciudad')
    search_fields = ('ciudad__nombre_ciudad',)
    list_editable = ('nombre',)
    #list_filter = ('codigo_dane','nombre_ciudad')
    ordering = ('id',)
