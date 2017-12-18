from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pedido
from producto.models import Talla
from django.views.generic import ListView
from django.db.models import Count, Sum, Value, CharField, Case, When
from django.db.models.functions import Concat
from .forms import PedidoForm
from producto.models import Producto
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from account.filters import UserFilter
from .filters import PedidoFilter
from filters.views import FilterMixin
import django_filters
from producto.filters import ProductoFilter
# from itertools import chain
# Vista de producto con soft delete, vista basada en funcion
# vista para listar todos los productos que no han sido eliminados

class PedidoList(ListView):
  model = Pedido
  template_name = 'pedidos/pedido_list.html'

  def get_queryset(self):
    return Pedido.objects.values('referencia_pedido').annotate(
      unidades_totales=Sum('unidades'), 
      dcount=Count('referencia_pedido'), 
      pagado=Sum('pagado'),
      unidades_vendidas=Sum('unidades_vendidas'),
      cliente=Concat('cliente__username', Value(''), output_field=CharField())
    )
        #     estado_general=Case(
        # When(estado='pendiente', then=Value('pendiente')),
        # default=Value('completado'),
        # output_field=CharField(),
        # )
class PedidoDetailList(ListView):
  model = Pedido
  template_name = 'pedidos/pedido_list_detail.html'

  def get_queryset(self):
    return Pedido.objects.filter(referencia_pedido=self.kwargs['pk'])

# vista para crear el pedido, aqui analizamos los datos de todo el pedido en la sesion
# y creamos las entradas en la base de datos
class CrearPedido(LoginRequiredMixin, FilterMixin, django_filters.views.FilterView):
  model = Producto
  paginate_by = 10
  template_name='pedidos/pedido_form.html'
  filterset_class = ProductoFilter
  success_url = reverse_lazy('pedido_list')

  def get_queryset(self):
    return self.model.objects.filter(deleted=False).order_by('id')

  def post(self, request, *args, **kwargs):

    # Cancelar pedido | limpiar sesion
    if 'cancelar' in request.POST:
      if 'pedidos' in request.session:
        request.session['pedidos'] = []
      if 'cliente' in request.session:
        request.session['cliente'] = ''

    # Realizar el pedido
    else:
      last_pedido = Pedido.objects.latest('referencia_pedido').referencia_pedido + 1
      cliente = User.objects.get(id=request.session['cliente'])
      producto = Producto.objects.get(id=request.session['pedidos'][0]['id_producto'])

      for pedido in request.session['pedidos']:
        Pedido.objects.create(
          referencia_pedido=last_pedido,
          cliente=cliente,
          producto=producto,
          unidades=pedido['cantidad'],
          talla=pedido['talla']
          )

      # limpiar la sesion
      if 'pedidos' in request.session:
        request.session['pedidos'] = []
      if 'cliente' in request.session:
        request.session['cliente'] = ''

    return HttpResponseRedirect(self.success_url)

# lista para que un cliente pueda ver los pedidos que ha realizado
class PedidoCliente(LoginRequiredMixin, ListView):
  model = Pedido
  template_name = 'pedidos/pedidos_cliente.html'

  # filtramos el queryset
  def get_queryset(self):
    return Pedido.objects.filter(cliente=self.request.user.id)

# primera vista al crear un pedido, nos lleva a una pantalla de seleccion de cliente
# para añadirlo a una variable de sesion
class ElegirCliente(LoginRequiredMixin, FilterMixin, django_filters.views.FilterView):
  model = User
  paginate_by = 10
  template_name="pedidos/elegir_cliente.html"
  filterset_class = UserFilter
  success_url = reverse_lazy('pedido_nuevo')

  def post(self, request, *args, **kwargs):
    user_id = request.POST.get('id')
    
    # añadir cliente a la sesion
    if user_id is not None:
      request.session['cliente'] = user_id

    # si hay algo en session.pedidos lo limpiamos
    if 'pedidos' in request.session:
      request.session['pedidos'] = []

    return HttpResponseRedirect(self.success_url)

# vista para ver y elegir las tallas disponibles de un producto
# estos son añadidos a la session
class ElegirTalla(LoginRequiredMixin, ListView):
  model = Producto
  model2 = Talla
  template_name = 'pedidos/elegir_talla.html'
  success_url = reverse_lazy('pedido_nuevo')

  # conseguimos las tallas que pertenecen al tallaje del producto
  def get_queryset(self):
    producto = self.model.objects.get(id=self.kwargs['pk'])
    tallas = self.model2.objects.filter(tallaje=producto.tallaje.id)
    for talla in tallas:
      talla.nombre_producto = producto.nombre
      talla.id_producto = producto.id
    return tallas

  def post(self, request, *args, **kwargs):
    producto = request.POST['producto']
    id_producto = request.POST['id_producto']

    # creamos la variable de sesion para los pedidos
    if 'pedidos' not in request.session:
      request.session['pedidos'] = []
      
    # obtenemos las tallas del formulario enviado y añadimos una entrada por talla 
    # a la sesion
    for e in request.POST:
      if e.isnumeric():
        cantidad = request.POST.getlist(e)[1]
        if int(cantidad) > 0:
          talla = request.POST.getlist(e)[0]
          request.session['pedidos'].append({ 'producto': producto, 'id_producto': id_producto, 'talla': talla, 'cantidad': cantidad })
          request.session.modified = True

    return HttpResponseRedirect(self.success_url)

# vista para ver todos los productos pedidos por un cliente
# aqui tenemos un textfield para modificar la cantidad de vendidos
class ProductoClienteList(LoginRequiredMixin, django_filters.views.FilterView, ListView):
  model = Pedido
  template_name = 'pedidos/producto_cliente.html'
  filterset_class = PedidoFilter
  success_url = reverse_lazy('productos_cliente')

  def get_queryset(self):
    return Pedido.objects.filter(cliente=self.request.user.id)

  def post(self, request, *args, **kwargs):
    suma = self.request.POST['cantidad']
    if suma.isnumeric():
      pedido = Pedido.objects.get(id=self.request.POST['id'])
      unidades_vendidas = pedido.unidades_vendidas + int(suma)
      if unidades_vendidas < pedido.unidades:
        Pedido.objects.filter(id=self.request.POST['id']).update(unidades_vendidas=unidades_vendidas)
    return HttpResponseRedirect(self.success_url)