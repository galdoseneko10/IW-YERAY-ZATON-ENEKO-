from django.db import models


# Create your models here.



# COMPONENTES
class Componente(models.Model):
    codigo_referencia = models.IntegerField()
    nombre_modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)


# PRODUCTOS
class Producto(models.Model):
    referencia = models.CharField(max_length=50)
    precio = models.FloatField()
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    tipo_componente = models.ManyToManyField(Componente)

#CLIENTE
class Cliente(models.Model):
    cif = models.CharField(max_length=50)
    nombre_empresa =  models.CharField(max_length=50)
    datos_contacto =  models.CharField(max_length=50)


# PEDIDO
class Pedido(models.Model):
    codigo_referencia = models.CharField(max_length=50)
    fecha = models.DateField()
    datos_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto_solicitado = models.ManyToManyField(Producto)
    cantidad_producto = models.IntegerField()
    precio_total = models.FloatField()
