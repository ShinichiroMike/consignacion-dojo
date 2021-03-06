from django.conf.urls import url
from .views import TallajesList, TallaOfTallajeList, TallajeCreate, talla_create_formset, TallaList, tallajes, ProductoList, ProductoDetail

urlpatterns = [
    url(r'^tallajes/(?P<pk>\d+)/$', tallajes, name='tallajes'),
    url(r'^tallajes/list/$', TallajesList, name='tallajes_list'),
    url(r'^producto/list/$', ProductoList.as_view(template_name='producto/filter_producto.html'), name='producto_list'),
    url(r'^producto/(?P<pk>\d+)/$', ProductoDetail.as_view(), name='producto_detail'),
    url(r'^tallaje/list/(?P<pk>\d+)/$', TallaOfTallajeList.as_view(), name='tallaje_list'),
    url(r'^tallaje/new/$', TallajeCreate.as_view(), name='tallaje_create'),
    url(r'^talla/new/$', talla_create_formset, name='talla_create'),
    url(r'^talla/list/$', TallaList, name='talla_list'),
]