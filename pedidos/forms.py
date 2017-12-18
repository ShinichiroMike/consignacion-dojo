from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
  name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name',}), required=False)

  class Meta:
    model = Pedido
    fields = ('cliente', 'producto', 'unidades', 'talla', )