from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.formsets import formset_factory
from django.contrib import messages
from django.views.generic import ListView
# modelos
from .models import Talla

#formularios
from .forms import TallaForm

# vista basada en clases
# lista que muestra las tallas de un tallaje seleccionado
class TallaOfTallajeList(ListView):
  model = Talla
  template_name = 'tallaje/list_tallaje.html'

  def get_queryset(self):
    return Talla.objects.filter(tallaje=self.kwargs['pk'])

# Vista de talla con soft delete, vista basada en funcion
# vista para listar todas las tallas que no han sido eliminadas
@login_required
@user_passes_test(lambda u: u.profile.is_admin == True)
def TallaList(request):
  if request.method == 'POST':
    pk = request.POST.get('id')
    if pk is not None:
      talla = Talla.objects.filter(pk=pk).update(deleted=True)
  tallas = Talla.objects.filter(deleted=False).order_by('id')
  context = {'tallas': tallas}
  return render(request, 'talla/list_talla.html', context)


# Talla Create View with formset options
# vista para el formulario para crear tallas, 
# con opciones para añadir dinamicamente el numero de talla que queramos de una vez
@login_required
@user_passes_test(lambda u: u.profile.is_admin == True)
def talla_create_formset(request):

  TallaFormset = formset_factory(TallaForm)

  if request.method == 'POST':
    talla_formset = TallaFormset(request.POST)

    if talla_formset.is_valid():

      new_tallas = []

      for  talla_form in talla_formset:
        nombre = talla_form.cleaned_data.get('nombre')
        incremento = talla_form.cleaned_data.get('incremento')
        tallaje = talla_form.cleaned_data.get('tallaje')
        new_tallas.append(Talla(nombre=nombre, incremento=incremento, tallaje=tallaje))

      try:
        Talla.objects.bulk_create(new_tallas)
        print(new_tallas)
        # And notify our users that it worked
        messages.success(request, 'You have updated your tallas.')
        return redirect(reverse_lazy('talla_list'))

      except: #If the transaction failed
        messages.error(request, 'There was an error saving your tallas.')
        return redirect(reverse_lazy('talla_create'))

  else:
    talla_formset = TallaFormset()

  context = {
    'talla_formset': talla_formset 
  }

  return render(request, 'talla/form_talla.html', context)