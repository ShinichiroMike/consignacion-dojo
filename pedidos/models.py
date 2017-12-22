from django.db import models
from django.contrib.auth.models import User
from producto.models import Producto
# Create your models here.

class Pedido(models.Model):
  referencia_pedido = models.IntegerField()
  cliente = models.ForeignKey(User)
  producto = models.ForeignKey(Producto)
  unidades = models.IntegerField()
  talla = models.CharField(max_length=3)
  deuda = models.FloatField(default=0)
  pagado = models.FloatField(default=0)
  unidades_vendidas = models.IntegerField(default=0)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  estado = models.CharField(max_length=100, default='pendiente')
  precio_total_unidad = models.FloatField()
  # total a pagar
  # modificador
