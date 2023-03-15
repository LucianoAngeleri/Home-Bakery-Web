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
        "productos": Producto.objects.all(),
      }  
    return render(request, "HomeBakery/producto.html", context)
def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
    else:
        producto_form = ProductoForm()

    context = {
        "form" : ProductoForm(),
        "productos": Producto.objects.all(),
      }  
    return render(request, "HomeBakery/producto.html", context)
def buscar_producto(request):
    criterio = request.GET.get("criterio")
    context = {
        "productos": Producto.objects.filter(nombre_producto__icontains=criterio).all(),
      }  
    return render(request, "HomeBakery/producto_lista.html", context)

class ProductoList(ListView):
    model = Producto
    template_name ="HomeBakery/producto_lista.html"
    context_object_name = "productos"
    