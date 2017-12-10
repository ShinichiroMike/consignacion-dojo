from django.conf.urls import url
from .views import PedidoList, PedidoDetailList, PedidoCliente, crearPedido

urlpatterns = [
    url(r'^pedidos/list/$', PedidoList.as_view(), name='pedido_list'),
    url(r'^pedidos/nuevo/$', crearPedido, name='pedido_nuevo'),
    url(r'^pedidos/list/(?P<pk>\d+)/$', PedidoDetailList.as_view(), name='pedido_list_detail'),
    url(r'^pedidos/cliente/$', PedidoCliente.as_view(), name='pedido_cliente'),
]