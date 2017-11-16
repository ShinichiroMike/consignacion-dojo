from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tallaje, Talla
from .forms import TallajeForm


# vista basada en funcion, login requerido 
# vista que muestra todos los tallajes
# y las tallas que pertenecen a el tallaje seleccionado
@login_required
def tallajes(request, pk):
  if request.method == 'GET':
    tallas = Talla.objects.filter(tallaje=pk)
    tallajes = Tallaje.objects.all()
  return render(request, 'tallaje/tallajes_and_tallas.html', {'tallas': tallas, 'tallajes': tallajes})

# vista basada en clases para crear el formulario que permite añadir nuevos tallajes
class TallajeCreate(LoginRequiredMixin, CreateView):
  model = Tallaje
  form_class = TallajeForm
  template_name = 'tallaje/form_tallaje.html'
  success_url = reverse_lazy('tallajes_list')

# Vista de tallajes con soft delete, vista basada en funcion
# vista para listar todos los tallajes que no han sido eliminados
@login_required
@user_passes_test(lambda u: u.profile.is_admin == True)
def TallajesList(request):
  if request.method == 'POST':
    pk = request.POST.get('id')
    if pk is not None:
      tallaje = Tallaje.objects.filter(pk=pk).update(deleted=True)
  tallajes = Tallaje.objects.filter(deleted=False).order_by('id')
  context = {'tallajes': tallajes}
  return render(request, 'tallaje/list_tallaje.html', context)