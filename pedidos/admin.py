from django.contrib import admin
from .models import Pedido
# Register your models here.

@admin.register(Pedido)
class Profile(admin.ModelAdmin):
  list_display = ('id', 'referencia_pedido', 'cliente', 'producto', 'unidades', 'talla', 'deuda', 'pagado', 'unidades_vendidas', 'fecha_creacion', 'estado')