from django import forms
from django.forms.formsets import BaseFormSet
from .models import Tallaje, Talla, Producto

class TallajeForm(forms.ModelForm):
  nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre',}), required=True)

  class Meta:
    model = Tallaje
    fields = ('nombre',)

class TallaForm(forms.ModelForm):
  nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre',}), required=True)
  incremento = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Incremento',}))
  tallaje = forms.ModelChoiceField(queryset=Tallaje.objects.all())

  class Meta:
    model = Talla
    fields = ('nombre', 'incremento', 'tallaje')