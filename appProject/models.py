from django.db import models

# Create your models here.


# COMPONENTES
class Componente(models.Model):
    codigo_referencia = models.IntegerField()
    nombre_modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_modelo


# PRODUCTOS
class Producto(models.Model):
    referencia = models.CharField(max_length=20)
    precio = models.FloatField()
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    tipo_componente = models.ManyToManyField(Componente)

    def __str__(self):
        return self.nombre

#CLIENTE
class Cliente(models.Model):
    cif = models.CharField(max_length=10)
    nombre_empresa = models.CharField(max_length=20)
    datos_contacto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_empresa


# PEDIDO
class Pedido(models.Model):
    codigo_referencia = models.CharField(max_length=10)
    fecha = models.DateField()
    datos_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto_solicitado = models.ManyToManyField(Producto)
    cantidad_producto = models.IntegerField()
    precio_total = models.FloatField()

    def __str__(self):
        return self.nombre
