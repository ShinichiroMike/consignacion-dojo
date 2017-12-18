from django.contrib.auth.models import User
import django_filters

class UserFilter(django_filters.FilterSet):
  username = django_filters.CharFilter(lookup_expr='icontains')

  class Meta:
      model = User
      fields = ['username', ]