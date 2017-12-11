from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
# from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Producto
from filters.views import FilterMixin
import django_filters

# Vista de producto con soft delete, vista basada en funcion
# vista para listar todos los productos que no han sido eliminados
# @login_required
# @user_passes_test(lambda u: u.profile.is_admin == True)
# def ProductoList(request):
#   if request.method == 'POST':
#     pk = request.POST.get('id')
#     if pk is not None:
#       producto = Producto.objects.filter(pk=pk).update(deleted=True)

#   productos_list = Producto.objects.filter(deleted=False).order_by('id')
  
#   page = request.GET.get('page', 1)

#   paginator = Paginator(productos_list, 10)
#   try:
#       productos = paginator.page(page)
#   except PageNotAnInteger:
#       productos = paginator.page(1)
#   except EmptyPage:
#       productos = paginator.page(paginator.num_pages)

#   context = {'productos': productos}
#   return render(request, 'producto/list_producto.html', context)
from .filters import ProductoFilter

class ProductoList(LoginRequiredMixin, FilterMixin, django_filters.views.FilterView):
  model = Producto
  paginate_by = 10
  filterset_class = ProductoFilter
  success_url = reverse_lazy('producto_list')

  def post(self, request, *args, **kwargs):
    id_producto = request.POST.get('id')

    if id_producto is not None:
      self.model.objects.filter(pk=id_producto).update(deleted=True)
      return HttpResponseRedirect(self.success_url)

  def get_queryset(self):
    return self.model.objects.filter(deleted=False).order_by('id')

# def ProductoList(request):
#     producto_list = Producto.objects.all()
#     producto_filter = ProductoFilter(request.GET, queryset=producto_list)
#     return render(request, 'producto/filter_producto.html', {'filter': producto_filter})