from .models import Pedido
import django_filters

class PedidoFilter(django_filters.FilterSet):
  producto = django_filters.CharFilter(name='producto__nombre', lookup_expr='icontains')
  cliente = django_filters.CharFilter(name='cliente', lookup_expr='icontains')
  color = django_filters.CharFilter(name='producto__color', lookup_expr='icontains')

  class Meta:
      model = Pedido
      fields = ['producto', 'referencia_pedido', 'cliente']