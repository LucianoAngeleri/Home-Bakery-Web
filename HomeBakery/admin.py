from django.contrib import admin

from HomeBakery.models import *

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ProductoPedido)