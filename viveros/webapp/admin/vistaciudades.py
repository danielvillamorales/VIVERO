from django.contrib import admin
from webapp.models.ciudades import Ciudades

@admin.register(Ciudades)
class Ciudadesadmin(admin.ModelAdmin):
    list_display = ('codigo_dane', 'nombre_ciudad')
    search_fields = ('codigo_dane', 'nombre_ciudad')
    list_editable = ('nombre_ciudad',)
    list_filter = ('codigo_dane','nombre_ciudad')
    ordering = ('id',)



