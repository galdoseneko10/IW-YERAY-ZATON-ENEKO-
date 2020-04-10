from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from appProject.models import Producto


class ProductosListView(ListView):
    model = Producto
    template_name = 'productos.html'
    queryset = Producto.objects.order_by('nombre')
    context_object_name = 'lista_productos'

    def get_context_data(self, **kwargs):
        context = super(ProductosListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Productos'
        return context


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto.html'

    def get_context_data(self, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del Producto'
        return context

