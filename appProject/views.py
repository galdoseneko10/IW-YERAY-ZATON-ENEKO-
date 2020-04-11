from appProject.forms import ProductoForm, PedidoForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from appProject.models import Producto
from appProject.models import Pedido
from django.views.generic.base import View






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

class CreateProductoView(View):
    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Publicar nueva noticia'
        }
        return render(request, 'producto_create.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'producto_create.html', {'form': form})


class PedidosListView(ListView):
    model = Pedido
    template_name = 'pedidos.html'
    queryset = Pedido.objects.order_by('codigo_referencia')
    context_object_name = 'lista_pedidos'

    def get_context_data(self, **kwargs):
        context = super(PedidosListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Pedidos'
        return context


class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido.html'

    def get_context_data(self, **kwargs):
        context = super(PedidoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del Pedido'
        return context


class CreatePedidosView(View):
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Añadir nuevo pedido'
        }
        return render(request, 'pedido_create.html', context)

    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pedidos')

        return render(request, 'pedido_create.html', {'form': form})


