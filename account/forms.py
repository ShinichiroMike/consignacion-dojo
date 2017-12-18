from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    #birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    class Meta:
        model = Profile
        fields = ('nombre', 'apellido', 'cif', 'direccion', 'localidad', 'codigo_postal', 'telefono', 'telefono_movil', 'forma_de_pago', 'numero_de_cuenta', 'deuda_cliente', 'estado_cliente')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
# class LoginForm(AuthenticationForm):
#   class Meta:
#     model = User
