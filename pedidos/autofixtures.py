from .models import Pedido
from django.contrib.auth.models import User
from autofixture import generators, register, AutoFixture
import random

class PedidoAutoFixture(AutoFixture):
    field_values = {
        'referencia_pedido': generators.StaticGenerator(1),
        'unidades': random.randint(100, 5000),
        'talla': random.choice(('M', 'L', 'XL', 'XXL')),
        'cliente': generators.InstanceSelector(User, limit_choices_to={'username':"juan"}),
    }

register(Pedido, PedidoAutoFixture)