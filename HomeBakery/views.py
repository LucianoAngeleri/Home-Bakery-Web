from django.shortcuts import render

def index(request):
    return render(request, "HomeBakery/index.html")
def pedido(request):
    return render(request, "HomeBakery/pedido.html")
def producto(request):
    return render(request, "HomeBakery/producto.html")
def cliente(request):
    return render(request, "HomeBakery/cliente.html")