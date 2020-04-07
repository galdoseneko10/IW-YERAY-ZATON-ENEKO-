from django.db import models


# Create your models here.



# COMPONENTES
class Componentes(models.Model):
    codigo_referencia = models.IntegerField()
    nombre_modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)


# PRODUCTOS
class Productos(models.Model):
    referencia = models.CharField(max_length=50)
    precio = models.IntegerField()
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    tipo_componente = models.ManyToManyField(Componentes)

#CLIENTE
class Cliente(models.Model):
    cif = models.CharField(max_length=50)
    nombre_empresa =  models.CharField(max_length=50)
    datos_contacto =  models.CharField(max_length=50)


# PEDIDO
class Pedidos(models.Model):
    codigo_referencia = models.CharField(max_length=50)
    fecha = models.DateField()
    datos_cliente = models.ManyToManyField(Cliente)
    producto_solicitado = models.ManyToManyField(Productos)
    cantidad_producto = models.IntegerField()
    precio_total = models.IntegerField()
