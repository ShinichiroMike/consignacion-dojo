from django.conf.urls import url
from .views import PedidoList, PedidoDetailList, PedidoCliente, CrearPedido, ElegirCliente, ElegirTalla, ProductoClienteList

urlpatterns = [
    url(r'^pedidos/list/$', PedidoList.as_view(), name='pedido_list'),
    url(r'^pedidos/nuevo/$', CrearPedido.as_view(), name='pedido_nuevo'),
    url(r'^pedidos/elegir_talla/(?P<pk>\d+)/$', ElegirTalla.as_view(), name='pedido_elegir_talla'),
    url(r'^pedidos/list/(?P<pk>\d+)/$', PedidoDetailList.as_view(), name='pedido_list_detail'),
    url(r'^pedidos/cliente/$', PedidoCliente.as_view(), name='pedido_cliente'),
    url(r'^productos/cliente/$', ProductoClienteList.as_view(), name='productos_cliente'),
    url(r'^pedidos/nuevo/cliente$', ElegirCliente.as_view(), name='pedido_nuevo_cliente'),
]