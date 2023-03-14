from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.producto, name='producto'),
    path('pedido/', views.pedido, name='pedido'),
    path('cliente/', views.cliente, name='cliente'),
]