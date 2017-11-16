from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto

# Vista de producto con soft delete, vista basada en funcion
# vista para listar todos los productos que no han sido eliminados
@login_required
@user_passes_test(lambda u: u.profile.is_admin == True)
def ProductoList(request):
  if request.method == 'POST':
    pk = request.POST.get('id')
    if pk is not None:
      producto = Producto.objects.filter(pk=pk).update(deleted=True)
  productos = Producto.objects.filter(deleted=False).order_by('id')
  context = {'productos': productos}
  return render(request, 'producto/list_producto.html', context)