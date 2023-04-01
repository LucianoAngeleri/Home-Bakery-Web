from django.db import models
from django.contrib.auth.models import User
class Producto(models.Model):
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="propietario")
    nombre_producto = models.CharField(max_length=50)
    descripcion_producto = models.TextField(default="", blank=True)
    precio = models.FloatField()
    imagen_producto = models.ImageField(upload_to="productos", blank=True, null=True)

    @property
    def imagen_producto_url(self):
        return self.imagen_producto.url if self.imagen_producto else ""

    def __str__(self):
        return f'{self.nombre_producto}'
class Pedido(models.Model):
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="cliente")
    fecha_pedido = models.DateField(auto_now_add=True)
    hora_pedido = models.TimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad_producto = models.IntegerField(default=0, null=True)

    @property
    def total_precio(self):
        return self.cantidad_producto * self.producto.precio

    def __str__(self):
        return f'Pedido ID:{self.id} - {self.cliente} - {self.fecha_pedido}'
# A implementar un carrito de productos
# class ProductoPedido(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
#     pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
#     cantidad_producto = models.IntegerField(default=0, null=True)

#     def __str__(self):
#         return f'ID:{self.id} - {self.producto} - {self.cantidad_producto}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)
    @property
    def imagen_avatar_url(self):
        return self.avatar.url if self.avatar else ""

    def __str__(self):
        return f'ID:{self.id} - {self.user} {self.nombre} {self.apellido}'