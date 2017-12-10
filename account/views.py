
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Profile
from django.forms.models import inlineformset_factory
from .forms import ProfileForm, EditUserForm
from django.views.generic import ListView

# vista para cargar el perfil de usuario
@login_required
def profile(request):
    return render(request, 'account/userprofile.html')

# vista para crear un usuario y perfil relacionado a este usuario
@user_passes_test(lambda u: u.is_anonymous, login_url='/accounts/profile')
def signup(request):
  if request.method == 'POST':
    user_form = UserCreationForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.refresh_from_db()  # Carga la instancia del Profile creado con el Signal
      profile_form = ProfileForm(request.POST, instance=user.profile)  # Recarga el formulario Profile con la instancia del Profile 
      profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method. 
      profile_form.save()  # Gracefully save the form
      user = authenticate(username=request.POST['username'], password=request.POST['password1'])
      if user is not None:
        login(request, user)
        return redirect('accounts:profile')
  else:
    user_form = UserCreationForm()
    profile_form = ProfileForm()
  return render(request, 'account/user_profile_form.html', {
    'user_form': user_form,
    'profile_form': profile_form
  })

# vista para editar al usuario
@login_required
def user_edit(request):
  if request.method == 'POST':
    user_form = EditUserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save() # guarda el usuario y el Signal guarda automaticamente la instancia del Profile dentro de User -> User.profile
      return redirect('accounts:profile')
  else:
    user_form = EditUserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
  return render(request, 'account/user_profile_form.html', {
    'user_form': user_form,
    'profile_form': profile_form
  })


class ClienteList(ListView):
  model = User
  template_name = 'account/cliente_list.html'
