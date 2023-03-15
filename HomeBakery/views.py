from django.shortcuts import render
from HomeBakery.models import Producto, Cliente, Pedido
from .forms import ProductoForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "HomeBakery/index.html")
def pedido(request):
    return render(request, "HomeBakery/pedido.html")
def producto(request):
    return render(request, "HomeBakery/producto.html")
def cliente(request):
    return render(request, "HomeBakery/cliente.html")
def mostrar_producto(request):
    context = {
        "form" : ProductoForm(),
      }  
    return render(request, "HomeBakery/producto.html", context)
class ProductoList(ListView):
    model = Producto
    template_name ="HomeBakery/producto_lista.html"
    