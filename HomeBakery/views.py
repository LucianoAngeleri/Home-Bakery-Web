from django.shortcuts import render
from HomeBakery.models import Producto, Cliente, Pedido
from .forms import ClienteForm, PedidoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
class ProductoUpdate(LoginRequiredMixin,UpdateView):
    model = Producto
    success_url = reverse_lazy("producto_lista")
    template_name ="HomeBakery/producto_actualizar.html"
    fields = '__all__'
class ProductoDelete(LoginRequiredMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy("producto_lista")
    context_object_name = "producto"
class ProductoCreate(LoginRequiredMixin,CreateView):
    model = Producto
    success_url = reverse_lazy("producto_lista")
    template_name ="HomeBakery/producto_crear.html"
    context_object_name = "producto"
    fields = '__all__'
class ProductoSearch(ListView):
    model = Producto
    template_name ="HomeBakery/producto_buscar.html"
    context_object_name = "productos"
    def get_queryset(self): 
        criterio = self.request.GET.get("criterio")
        result = Producto.objects.filter(nombre_producto__icontains=criterio).all()
        return result
class ClienteList(ListView):
    model = Cliente
    template_name ="HomeBakery/cliente_lista.html"
    context_object_name = "clientes"    
class PedidoList(ListView):
    model = Pedido
    template_name ="HomeBakery/pedido_lista.html"
    context_object_name = "pedidos"  
class PedidoDetail(DetailView):
    model = Pedido
    template_name ="HomeBakery/pedido_detalle.html"
    context_object_name = "pedido"
class PedidoUpdate(LoginRequiredMixin,UpdateView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista")
    template_name ="HomeBakery/pedido_actualizar.html"
    fields = '__all__'
class PedidoDelete(LoginRequiredMixin,DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista")
    context_object_name = "pedido"
class PedidoCreate(LoginRequiredMixin,CreateView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista")
    template_name ="HomeBakery/pedido_crear.html"
    context_object_name = "pedido"
    fields = '__all__'  
class ClienteDetail(DetailView):
    model = Cliente
    template_name ="HomeBakery/cliente_detalle.html"
    context_object_name = "cliente"
class Login(LoginView):
    next_page = reverse_lazy("index")
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("index")
class Logout(LogoutView):
    template_name = 'registration/logout.html'
