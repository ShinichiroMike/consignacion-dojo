from django.contrib import admin
from .models import Profile, Tarifa
# Register your models here.

@admin.register(Profile)
class Profile(admin.ModelAdmin):
  list_display = ('user', 'is_admin', 'fecha_alta', 'nombre', 'apellido', 'cif', 'direccion', 'localidad', 'codigo_postal', 'telefono', 'telefono_movil', 'forma_de_pago', 'numero_de_cuenta', 'deuda_cliente', 'estado_cliente' )

@admin.register(Tarifa)
class Tarifa(admin.ModelAdmin):
  list_display = ('nombre', 'descripcion', 'modificador', )

  def __str__(self):
    return '{}'.format(self.nombre)