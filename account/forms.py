from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date', 'is_admin')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', )

# class LoginForm(AuthenticationForm):
#   class Meta:
#     model = User
