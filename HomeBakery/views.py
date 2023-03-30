from django.shortcuts import render
from HomeBakery.models import Producto, Cliente, Pedido
from .forms import ProductoForm, ClienteForm, PedidoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "HomeBakery/index.html")
def pedido(request):
    return render(request, "HomeBakery/pedido.html")
def mostrar_pedido(request):
    context = {
        "form" : PedidoForm(),
        "pedidos": Pedido.objects.all(),
        }  
    return render(request, "HomeBakery/pedido.html", context)
def agregar_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        if pedido_form.is_valid():
            pedido_form.save()
    else:
        pedido_form = PedidoForm()

    context = {
        "form" : PedidoForm(),
        "pedidos": Pedido.objects.all(),
      }  
    return render(request, "HomeBakery/pedido.html", context)
def producto(request):
    return render(request, "HomeBakery/producto.html")
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
def cliente(request):
    return render(request, "HomeBakery/cliente.html")
def mostrar_cliente(request):
    context = {
        "form" : ClienteForm(),
        "clientes": Cliente.objects.all(),
        }  
    return render(request, "HomeBakery/cliente.html", context)
def agregar_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
    else:
        cliente_form = ClienteForm()

    context = {
        "form" : ClienteForm(),
        "clientes": Cliente.objects.all(),
      }  
    return render(request, "HomeBakery/cliente.html", context)

class ProductoList(ListView):
    model = Producto
    template_name ="HomeBakery/producto_lista.html"
    context_object_name = "productos"
class ProductoDetail(DetailView):
    model = Producto
    template_name ="HomeBakery/producto_detalle.html"
    context_object_name = "producto"
class ProductoUpdate(UpdateView):
    model = Producto
    success_url = reverse_lazy("producto_lista")
    template_name ="HomeBakery/producto_actualizar.html"
    fields = '__all__'
class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy("producto_lista")
    context_object_name = "producto"
class ProductoCreate(CreateView):
    model = Producto
    success_url = reverse_lazy("producto_lista")
    template_name ="HomeBakery/producto_crear.html"
    context_object_name = "producto"
    fields = '__all__'
class ClienteList(ListView):
    model = Cliente
    template_name ="HomeBakery/cliente_lista.html"
    context_object_name = "clientes"    
class PedidoList(ListView):
    model = Pedido
    template_name ="HomeBakery/pedido_lista.html"
    context_object_name = "pedidos"    
class ClienteDetail(DetailView):
    model = Cliente
    template_name ="HomeBakery/cliente_detalle.html"
    context_object_name = "cliente"
class PedidoDetail(DetailView):
    model = Pedido
    template_name ="HomeBakery/pedido_detalle.html"
    context_object_name = "pedido"