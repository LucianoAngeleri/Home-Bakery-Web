from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.mostrar_producto, name='producto'),
    path('producto/agregar', views.agregar_producto, name='agregar_producto'),
    path('producto/lista', views.ProductoList.as_view() , name='producto_lista'),
    path('producto/<pk>/detalle', views.ProductoDetail.as_view() , name='producto_detalle'),
    path('producto/buscar', views.buscar_producto, name='buscar_producto'),
    path('pedido/', views.mostrar_pedido, name='pedido'),
    path('pedido/agregar', views.agregar_pedido, name='agregar_pedido'),
    path('pedido/lista', views.PedidoList.as_view() , name='pedido_lista'),
    path('pedido/<pk>/detalle', views.PedidoDetail.as_view() , name='pedido_detalle'),
    path('cliente/', views.mostrar_cliente, name='cliente'),
    path('cliente/agregar', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/lista', views.ClienteList.as_view() , name='cliente_lista'),
    path('cliente/<pk>/detalle', views.ClienteDetail.as_view() , name='cliente_detalle'),
]