from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.mostrar_producto, name='producto'),
    path('producto/agregar', views.agregar_producto, name='agregar_producto'),
    path('producto/lista', views.ProductoList.as_view() , name='producto_lista'),
    path('pedido/', views.pedido, name='pedido'),
    path('cliente/', views.cliente, name='cliente'),
]