from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'Cliente ID:{self.id} - {self.nombre} {self.apellido}'

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    descripcion_producto = models.TextField(default="", blank=True)
    precio = models.FloatField()
    imagen_producto = models.ImageField(upload_to="productos", blank=True, null=True)

    @property
    def imagen_producto_url(self):
        return self.imagen_producto.url if self.imagen_producto else ""

    def __str__(self):
        return f'Producto ID:{self.id} - {self.nombre_producto}'
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL, null=True)
    fecha_pedido = models.DateField(auto_now_add=True)
    hora_pedido = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido ID:{self.id} - {self.cliente} - {self.fecha_pedido}'
class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    cantidad_producto = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f'ID:{self.id} - {self.producto} - {self.cantidad_producto}'