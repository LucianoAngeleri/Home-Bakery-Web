from HomeBakery.models import Producto, Pedido, Profile, Mensaje
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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
class IndexView(TemplateView):
    template_name = "HomeBakery/index.html"
class AboutView(TemplateView):
    template_name = "HomeBakery/about.html"

class ProductoView(TemplateView):
    template_name = "HomeBakery/producto.html"
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
    success_url = reverse_lazy("producto_lista_mine")
    template_name ="HomeBakery/producto_actualizar.html"
    fields = '__all__'
class ProductoDelete(LoginRequiredMixin,PermisosProductoSoloPropietario,DeleteView):
    model = Producto
    success_url = reverse_lazy("producto_lista_mine")
    context_object_name = "producto"
class ProductoCreate(LoginRequiredMixin,CreateView):
    model = Producto
    success_url = reverse_lazy("producto_lista_mine")
    template_name ="HomeBakery/producto_crear.html"
    context_object_name = "producto"
    fields = ['nombre_producto','descripcion_producto','precio','imagen_producto']

    def form_valid(self,form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)
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
    success_url = reverse_lazy("pedido_lista_mine")
    template_name ="HomeBakery/pedido_actualizar.html"
    fields = '__all__'
class PedidoDelete(LoginRequiredMixin,PermisosPedidoSoloCliente,DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista_mine")
    context_object_name = "pedido"
class PedidoCreate(LoginRequiredMixin,CreateView):
    model = Pedido
    success_url = reverse_lazy("pedido_lista_mine")
    template_name ="HomeBakery/pedido_crear.html"
    context_object_name = "pedido"
    fields = ['producto','cantidad_producto']  
    
    def form_valid(self,form):
        form.instance.cliente = self.request.user
        return super().form_valid(form)
class Login(LoginView):
    next_page = reverse_lazy("index")
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("login")
class Logout(LogoutView):
    template_name = 'registration/logout.html'
class ProfileUpdate(UserPassesTestMixin,UpdateView):
    model = Profile
    success_url = reverse_lazy("index")
    template_name ="HomeBakery/profile_actualizar.html"
    fields = ['nombre','apellido','email','telefono','direccion','fecha_nacimiento','avatar']

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()
class ProfileCreate(CreateView):
    model = Profile
    success_url = reverse_lazy("index")
    template_name ="HomeBakery/profile_crear.html"
    context_object_name = "profile"
    fields =['nombre','apellido','email','telefono','direccion','fecha_nacimiento','avatar']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy("mensaje_crear")
    template_name ="HomeBakery/mensaje_crear.html"
    fields = ['mensaje', 'email']

    def form_valid(self, form):
        form.instance.destinatario = User.objects.get(username='admin')
        return super().form_valid(form)
class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mensaje_lista_mine")
    
    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
class MensajeMineList(LoginRequiredMixin ,ListView):
    model = Mensaje
    template_name = "HomeBakery/mensaje_lista.html"
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user)