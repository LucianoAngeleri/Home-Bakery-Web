from django import forms
from .models import Producto, Cliente, Pedido, ProductoPedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = "__all__"