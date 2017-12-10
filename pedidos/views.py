from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Pedido
from django.views.generic import ListView
from django.db.models import Count, Sum, Value, CharField, Case, When
from django.db.models.functions import Concat
from .forms import PedidoForm
from producto.models import Producto
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

# Es una prueba. Hay que cambiar esta vista.
# def crearPedido(request):
#   if request.method == 'POST':
#     pass
#   else:
#     pedido_form = PedidoForm()
#   return render(request, 'pedidos/pedido_form.html', { 'form': pedido_form })

def crearPedido(request):
  if request.method == 'POST':
    print('post!')
    print(request.POST)
    # pedido_form = PedidoForm()
  productos = Producto.objects.all()
  return render(request, 'pedidos/pedido_form.html', { 'productos': productos })

class PedidoCliente(ListView):
  model = Pedido
  template_name = 'pedidos/pedido_cliente.html'

  def get_queryset(self):
    return Pedido.objects.filter(cliente=self.request.user.id)