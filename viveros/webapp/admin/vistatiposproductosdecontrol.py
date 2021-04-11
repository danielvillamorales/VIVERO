from django.contrib import admin
from webapp.models.tipos_productos_control import Tiposproductoscontrol

@admin.register(Tiposproductoscontrol)
class Tiposproductoscontroladmin(admin.ModelAdmin):
    list_display = ('tipo_producto','periodo_carencia', 'nombre','fecha_ua' )
    search_fields = ('tipo_producto',)
    list_filter = ('periodo_carencia',)
    ordering = ('id',)
