from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'{self.id} - {self.nombre} {self.apellido}'

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_producto = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.nombre_producto} - $ {self.precio_producto} - {self.cantidad_producto} un.'
class Pedido(models.Model):
    fecha_pedido = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos_en_pedido = models.ManyToManyField(Producto)

    def __str__(self):
        return f'{self.id} - {self.cliente} - Fecha:{self.fecha_pedido}'
