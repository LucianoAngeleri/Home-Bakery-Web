from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.producto, name='producto'),
    path('producto/lista', views.ProductoList.as_view() , name='producto_lista'),
    path('producto/<pk>/detalle', views.ProductoDetail.as_view() , name='producto_detalle'),
    path('producto/<pk>/actualizar', views.ProductoUpdate.as_view() , name='producto_actualizar'),
    path('producto/<pk>/borrar', views.ProductoDelete.as_view() , name='producto_borrar'),
    path('producto/crear', views.ProductoCreate.as_view() , name='producto_crear'),
    path('producto/buscar', views.ProductoSearch.as_view(), name='producto_buscar'),
    path('pedido/', views.mostrar_pedido, name='pedido'),
    path('pedido/agregar', views.agregar_pedido, name='agregar_pedido'),
    path('pedido/lista', views.PedidoList.as_view() , name='pedido_lista'),
    path('pedido/<pk>/detalle', views.PedidoDetail.as_view() , name='pedido_detalle'),
    path('cliente/', views.mostrar_cliente, name='cliente'),
    path('cliente/agregar', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/lista', views.ClienteList.as_view() , name='cliente_lista'),
    path('cliente/<pk>/detalle', views.ClienteDetail.as_view() , name='cliente_detalle'),
    path('login/', views.Login.as_view() , name='login'),
    path('signup/', views.SignUp.as_view() , name='signup'),
    path('logout/', views.Logout.as_view() , name='logout'),
]