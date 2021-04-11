from django.contrib import admin
from webapp.models.ciudades import Ciudades
from webapp.models.productores import Productores
from webapp.models.productores_viveros import Productores_viveros
from webapp.models.viveros import Viveros
from webapp.models.tipos_de_labores import Tiposlabores
from webapp.models.productos_de_control import Productoscontrol
from webapp.models.tipos_productos_control import Tiposproductoscontrol
from webapp.models.labores import Labores


admin.site.register(Ciudades)
admin.site.register(Productores)
admin.site.register(Productores_viveros)
admin.site.register(Viveros)
admin.site.register(Tiposlabores)
admin.site.register(Productoscontrol)
admin.site.register(Tiposproductoscontrol)
admin.site.register(Labores)






