from django.db import models

# 
# tallaje model
class Tallaje(models.Model):
  nombre = models.CharField(max_length=100, unique=True)
  deleted = models.BooleanField(default=False)

  def __str__(self):
    return '{}'.format(self.nombre)

'''
Validators
Aplicar uppercase al nombre de la talla
'''
# talla model
class Talla(models.Model):
  nombre = models.CharField(max_length=3)
  incremento = models.FloatField()
  tallaje = models.ForeignKey(Tallaje, on_delete=models.CASCADE)
  deleted = models.BooleanField(default=False)

# productos model
class Producto(models.Model):
  nombre = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  precio_base = models.FloatField()
  tallaje = models.ForeignKey(Tallaje)
  deleted = models.BooleanField(default=False)

  def __str__(self):
    return '{}'.format(self.nombre)
