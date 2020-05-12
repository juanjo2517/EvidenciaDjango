from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Autores, Cliente, Categorias, Libros, LibroPorAutor, PedidosCliente
# Create your views here.

def index(request):
    return render(request, 'index.html') #index.html es el template

"""VISTAS BASADAS EN CLASES. SON MÁS FACILES DE USAR
ListView es una clase que es para listar datos rapidamente"""


def listar_cliente(request):
    busqueda = request.POST.get("buscar")
    clientes = Cliente.objects.all()

    if busqueda:
        clientes = Cliente.objects.filter(
            Q(identificacion__icontains = busqueda) | 
            Q(nombres__icontains = busqueda) |
            Q(apellidos__icontains = busqueda) |
            Q(correo_electronico__icontains = busqueda)
        ).distinct()
         

    return render(request, 'clientes.html', {'clientes':clientes})



class ListarCliente(ListView):
    model = Cliente #Modelo al cual se va listar
    template_name = 'clientes.html' #Nombre del template
    context_object_name = 'clientes' #Como se va a llamar el diccionario que trae los datos

def buscar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    
    return render(request, 'clientes.html', {'Onecliente':cliente})

"""Para entender mejor vaya al template clientes.html, está en la carpeta Templates.
Vea el inicio del archivo"""


class ListarAutor(ListView):
    model = Autores
    template_name = 'autor.html'
    context_object_name = 'autores'

class ListarCategoria(ListView):
    model = Categorias
    template_name = 'categoria.html'
    context_object_name = 'categorias'

class ListarLibro(ListView):
    model = Libros
    template_name = 'libro.html'
    context_object_name = 'libros'

class ListarLibroPorAutor(ListView):
    model = LibroPorAutor
    template_name = 'libro_por_autor.html'
    context_object_name = 'libro_por_autores'

class ListarPedidoCliente(ListView):
    model = PedidosCliente
    template_name = 'pedidos.html'
    context_object_name = 'pedidos'
