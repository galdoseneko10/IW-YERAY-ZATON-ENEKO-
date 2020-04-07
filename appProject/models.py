from django.db import models

# Create your models here.

#PEDIDO



#PRODUCTOS




#COMPONENTES
class Componentes (models.Model):

    codigo_referencia = models.IntegerField()
    nombre_modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)