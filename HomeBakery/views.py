from django.shortcuts import render
from HomeBakery.models import Producto, Cliente, Pedido, ProductoPedido
from .forms import ClienteForm, PedidoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "HomeBakery/index.html")
def producto(request):
    return render(request, "HomeBakery/producto.html")
def cliente(request):
    return render(request, "HomeBakery/cliente.html")
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
class ClienteList(ListView):
    model = Cliente
    template_name ="HomeBakery/cliente_lista.html"
    context_object_name = "clientes"    
class ClienteDetail(DetailView):
    model = Cliente
    template_name ="HomeBakery/cliente_detalle.html"
    context_object_name = "cliente"
class ClienteUpdate(LoginRequiredMixin,UpdateView):
    model = Cliente
    success_url = reverse_lazy("cliente_lista")
    template_name ="HomeBakery/cliente_actualizar.html"
    fields = '__all__'
class ClienteDelete(LoginRequiredMixin,DeleteView):
    model = Cliente
    success_url = reverse_lazy("cliente_lista")
    context_object_name = "cliente"
class ClienteCreate(LoginRequiredMixin,CreateView):
    model = Cliente
    success_url = reverse_lazy("cliente_lista")
    template_name ="HomeBakery/cliente_crear.html"
    context_object_name = "cliente"
    fields = '__all__'  
class Login(LoginView):
    next_page = reverse_lazy("index")
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("index")
class Logout(LogoutView):
    template_name = 'registration/logout.html'
