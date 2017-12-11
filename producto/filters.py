from .models import Producto
import django_filters

class ProductoFilter(django_filters.FilterSet):
  nombre = django_filters.CharFilter(lookup_expr='icontains')
  color = django_filters.CharFilter(lookup_expr='icontains')

  class Meta:
      model = Producto
      fields = ['nombre', 'color', 'precio_base', ]