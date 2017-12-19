from .models import Producto
import django_filters

class ProductoFilter(django_filters.FilterSet):
  nombre = django_filters.CharFilter(lookup_expr='icontains')
  color = django_filters.CharFilter(lookup_expr='icontains')
  precio_base = django_filters.NumberFilter()
  precio_base__gt = django_filters.NumberFilter(label="precio minimo", name='precio_base', lookup_expr='gt')
  precio_base__lt = django_filters.NumberFilter(name='precio_base', lookup_expr='lt')

  class Meta:
      model = Producto
      fields = ['nombre', 'color', ]