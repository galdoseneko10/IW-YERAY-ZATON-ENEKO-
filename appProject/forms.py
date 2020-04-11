from django import forms
from .models import Producto, Pedido, Cliente, Componente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '_all_'
