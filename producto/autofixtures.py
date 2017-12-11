from .models import Producto
from autofixture import generators, register, AutoFixture
import random

class ProductoAutoFixture(AutoFixture):
    field_values = {
        'color': random.choice(('blanco','negro', 'azul', 'verde')),
        'precio_base': random.randint(8, 25)
    }

register(Producto, ProductoAutoFixture)