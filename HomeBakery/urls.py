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
    path('pedido/lista', views.PedidoList.as_view() , name='pedido_lista'),
    path('pedido/crear', views.PedidoCreate.as_view(), name='pedido_crear'),
    path('pedido/<pk>/detalle', views.PedidoDetail.as_view() , name='pedido_detalle'),
    path('pedido/<pk>/actualizar', views.PedidoUpdate.as_view() , name='pedido_actualizar'),
    path('pedido/<pk>/borrar', views.PedidoDelete.as_view() , name='pedido_borrar'),
    path('login/', views.Login.as_view() , name='login'),
    path('signup/', views.SignUp.as_view() , name='signup'),
    path('logout/', views.Logout.as_view() , name='logout'),
    path('producto/lista/mine', views.ProductoMineList.as_view() , name='producto_lista_mine'),
    path('pedido/lista/mine', views.PedidoMineList.as_view() , name='pedido_lista_mine'),
]

