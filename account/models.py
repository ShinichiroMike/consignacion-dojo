from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tarifa(models.Model):
  modificador = models.FloatField(default=0)
  nombre = models.CharField(default='', max_length=250, blank=True)
  descripcion = models.TextField(max_length=500, blank=True)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  nombre = models.CharField(default='', max_length=250, blank=False)
  apellido = models.CharField(default='', max_length=250, blank=False)
  cif = models.IntegerField(null=True, blank=True)
  is_admin = models.BooleanField(default=False)
  direccion = models.CharField(default='', max_length=250, blank=True)
  localidad = models.CharField(default='', max_length=250, blank=True)
  provincia = models.CharField(default='', max_length=250, blank=True)
  codigo_postal = models.IntegerField(null=True, blank=True)
  telefono = models.IntegerField(null=True, blank=True)
  telefono_movil = models.IntegerField(null=True, blank=True)
  forma_de_pago = models.CharField(null=True, max_length=250, blank=True)
  numero_de_cuenta = models.IntegerField(null=True, blank=True)
  fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
  tarifa = models.ForeignKey(Tarifa, null=True)
  deuda_cliente = models.IntegerField(default=0, blank=True)
  estado_cliente = models.CharField(default='activo', max_length=250, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
  if created:
      Profile.objects.create(user=instance)
  instance.profile.save()