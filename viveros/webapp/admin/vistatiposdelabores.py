from django.contrib import admin
from webapp.models.tipos_de_labores import Tiposlabores

@admin.register(Tiposlabores)
class Tipolaboradmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)
    #list_editable = ('descripcion',)
    #list_filter = ('codigo_dane','nombre_ciudad')
    ordering = ('id',)