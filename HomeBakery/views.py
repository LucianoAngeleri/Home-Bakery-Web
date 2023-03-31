from django.shortcuts import render
from HomeBakery.models import Producto, Pedido, ProductoPedido
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PermisosProductoSoloPropietario(UserPassesTestMixin):
    def test_func(self):
        user_id = self.request.user.id
        producto_id = self.kwargs.get("pk")
        return Producto.objects.filter(propietario=user_id, id=producto_id).exists()
class PermisosPedidoSoloCliente(UserPassesTestMixin):
    def test_func(self):
        user_id = self.request.user.id
        pedido_id = self.kwargs.get("pk")
        return Pedido.objects.filter(cliente=user_id, id=pedido_id).exists()
def index(request):
    return render(request, "HomeBakery/index.html")
def producto(request):
    return render(request, "HomeBakery/producto.html")
class ProductoList(ListView):
    model = Producto
    template_name ="HomeBakery/producto_lista.html"
    context_object_name = "productos"
class ProductoMineList(LoginRequiredMixin, ListView):
    model = Producto
    template_name ="HomeBakery/producto_lista.html"
    context_object_name = "productos"
    def get_queryset(self):
        return Producto.objects.filter(propietario=self.request.user.id).all()
class ProductoDetail(DetailView):
    model = Producto
    template_name ="HomeBakery/producto_detalle.html"
    context_object_name = "producto"
class ProductoUpdate(LoginRequiredMixin,PermisosProductoSoloPropietario,UpdateView):
    model = Producto
    success_url = reverse_lazy("producto_lista")
    template_name ="HomeBakery/producto_actualizar.html"
    fields = '__all__'
class ProductoDelete(LoginRequiredMixin,PermisosProductoSoloPropietario,DeleteView):
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
class PedidoMineList(LoginRequiredMixin,ListView):
    model = Pedido
    template_name ="HomeBakery/pedido_lista.html"
    context_object_name = "pedidos"
    def get_queryset(self):
        return Pedido.objects.filter(cliente=self.request.user.id).all()
class PedidoDetail(DetailView):
    model = Pedido
    template_name ="HomeBakery/pedido_detalle.html"
    context_object_name = "pedido"
class PedidoUpdate(LoginRequiredMixin,PermisosPedidoSoloCliente,UpdateView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista")
    template_name ="HomeBakery/pedido_actualizar.html"
    fields = '__all__'
class PedidoDelete(LoginRequiredMixin,PermisosPedidoSoloCliente,DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista")
    context_object_name = "pedido"
class PedidoCreate(LoginRequiredMixin,CreateView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista")
    template_name ="HomeBakery/pedido_crear.html"
    context_object_name = "pedido"
    fields = '__all__'  
class Login(LoginView):
    next_page = reverse_lazy("index")
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("index")
class Logout(LogoutView):
    template_name = 'registration/logout.html'
