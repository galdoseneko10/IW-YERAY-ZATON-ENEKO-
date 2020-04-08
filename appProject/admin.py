from django.contrib import admin
from .models import Cliente, Componente, Producto, Pedido

# Register your models here.


admin.site.register(Cliente)
admin.site.register(Componente)
admin.site.register(Producto)
admin.site.register(Pedido)
