from django.contrib import admin
from .models import Cliente, Componentes, Productos, Pedidos

# Register your models here.


admin.site.register(Cliente)
admin.site.register(Componentes)
admin.site.register(Productos)
admin.site.register(Pedidos)
