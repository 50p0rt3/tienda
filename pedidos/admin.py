from django.contrib import admin
#V17
from pedidos.models import Cliente, Articulo, Pedido

# Register your models here.
#V18 - Mostrar mas campos y un campo de busqueda
class ClientesAdmin(admin.ModelAdmin):
    list_display=("name","address","phone")
    search_fields=("name","phone")

#V19 - Agregar Filtros - Cambiar idioma
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("section",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("number","date")
    list_filter=("date",)
    date_hierarchy="date"


#V17 - Agregar los modelos al panel Administracion
admin.site.register(Cliente,ClientesAdmin)
admin.site.register(Articulo,ArticulosAdmin)
admin.site.register(Pedido,PedidosAdmin)


