from django.contrib.auth.models import User
import django_filters

class UserFilter(django_filters.FilterSet):
  username = django_filters.CharFilter(lookup_expr='icontains')
  cif = django_filters.CharFilter(name='profile__cif', lookup_expr='icontains')
  nombre = django_filters.CharFilter(name='profile__nombre', lookup_expr='icontains')
  apellido = django_filters.CharFilter(name='profile__apellido', lookup_expr='icontains')

  class Meta:
      model = User
      fields = ['username', 'cif']