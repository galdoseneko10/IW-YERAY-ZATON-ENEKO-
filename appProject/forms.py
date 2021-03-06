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
        widgets = {
        'fecha': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'

