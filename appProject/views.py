from appProject.forms import ProductoForm, PedidoForm, ClienteForm, ComponenteForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from appProject.models import Producto, Cliente, Componente
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
            'titulo_pagina': 'Añadir nuevo producto'
        }
        return render(request, 'producto_create.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')

        return render(request, 'producto_create.html', {'form': form})


def delete_producto(request, producto_id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Producto.objects.get(id=producto_id)
    instancia.delete()
    return redirect('productos')


def edit_producto(request, producto_id):
    #Recuperamos la instancia de la persona
    instancia = Producto.objects.get(id=producto_id)

    # Creamos el formulario con los datos de la instancia
    form = ProductoForm(instance=instancia)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = ProductoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('productos')

    # Si llegamos al final renderizamos el formulario
    return render(request, "producto_edit.html", {'form': form})


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
        data = {'clientes':Cliente.objects.all(),
                'productos':Producto.objects.all()
        }
        context = {
            'data' : data,
            'form': form,
            'titulo_pagina': 'Crear nuevo pedido'
        }
        return render(request, 'pedido_create.html', context)

    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        print(request.POST.getlist('poducto_solicitado[]'))

        if form.is_valid():

            form.save()
            return redirect('pedidos')

        return render(request, 'pedido_create.html', {'form': form})

def delete_pedido(request, pedido_id):
    # Recuperamos la instancia del componente y lo borramos
    instancia = Pedido.objects.get(id=pedido_id)
    instancia.delete()
    return redirect('pedidos')


def edit_pedido(request, pedido_id):
    #Recuperamos la instancia del componente
    instancia = Pedido.objects.get(id=pedido_id)

    # Creamos el formulario con los datos de la instancia
    form = PedidoForm(instance=instancia)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = PedidoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
             # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('pedidos')

    # Si llegamos al final renderizamos el formulario
    return render(request, "pedido_edit.html", {'form': form})

class ClientesListView(ListView):
    model = Cliente
    template_name = 'clientes.html'
    queryset = Cliente.objects.order_by('nombre_empresa')
    context_object_name = 'lista_clientes'

    def get_context_data(self, **kwargs):
        context = super(ClientesListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Clientes'
        return context


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Datos del Cliente'
        return context

class CreateClienteView(View):
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        context = {
            'form': form,
            'titulo_pagina': 'Añadir nuevo Cliente'
        }
        return render(request, 'cliente_create.html', context)

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')

        return render(request, 'cliente_create.html', {'form': form})

def delete_cliente(request, cliente_id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Cliente.objects.get(id=cliente_id)
    instancia.delete()
    return redirect('clientes')


def edit_cliente(request, cliente_id):
    #Recuperamos la instancia de la persona
    instancia = Cliente.objects.get(id=cliente_id)

    # Creamos el formulario con los datos de la instancia
    form = ClienteForm(instance=instancia)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = ClienteForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
             # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('clientes')

    # Si llegamos al final renderizamos el formulario
    return render(request, "cliente_edit.html", {'form': form})

# COMPONETES

class ComponentesListView(ListView):
    model = Componente
    template_name = 'componentes.html'
    queryset = Componente.objects.order_by('nombre_modelo')
    context_object_name = 'lista_componentes'

    def get_context_data(self, **kwargs):
        context = super(ComponentesListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Componentes'
        return context


class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'componente.html'

    def get_context_data(self, **kwargs):
        context = super(ComponenteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Datos del Componente'
        return context

class CreateComponenteView(View):
    def get(self, request, *args, **kwargs):
        form = ComponenteForm()
        context = {
            'form': form,
            'titulo_pagina': 'Añadir nuevo Componente'
        }

        return render(request, 'componente_create.html', context)

    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('componentes')

        return render(request, 'componente_create.html', {'form': form})

def delete_componente(request, componente_id):
    # Recuperamos la instancia del componente y lo borramos
    instancia = Componente.objects.get(id=componente_id)
    instancia.delete()
    return redirect('componentes')


def edit_componente(request, componente_id):
    #Recuperamos la instancia del componente
    instancia = Componente.objects.get(id=componente_id)

    # Creamos el formulario con los datos de la instancia
    form = ComponenteForm(instance=instancia)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = ComponenteForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
             # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('componentes')

    # Si llegamos al final renderizamos el formulario
    return render(request, "componente_edit.html", {'form': form})


def paginaprincipal(request):
    return render(request,"paginaprincipal.html")
