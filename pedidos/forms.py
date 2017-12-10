from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):

  class Meta:
    model = Pedido
    fields = ('cliente', 'producto', 'unidades', 'talla', )