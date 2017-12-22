from django.contrib import admin
from .models import Tallaje, Talla, Producto


# Register your models here.

@admin.register(Tallaje)
class Tallaje(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'deleted')

@admin.register(Talla)
class Tallaje(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'tallaje', 'incremento', 'deleted')

@admin.register(Producto)
class Producto(admin.ModelAdmin):
  list_display = ('nombre', 'color', 'tallaje', 'precio_base', 'deleted')