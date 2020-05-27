from django.shortcuts import render
from django.contrib import auth 
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Autores, Cliente, Categorias, Libros, PedidosCliente
from .forms import ClienteForm, AutorForm, CategoriaForm, LibroForm

# Create your views here.

def index(request):
    return render(request, 'index.html') #index.html es el template


#--------------Views para Cliente--------------#

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


class AgregarCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'modals/cliente/agregar_cliente.html'
    success_url = reverse_lazy('libreria:cliente')
    

class EditarCliente(UpdateView):
    model = Cliente
    template_name = 'modals/cliente/editar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('libreria:cliente')
    

class EliminarCliente(DeleteView):
    model = Cliente
    template_name = 'modals/cliente/eliminar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('libreria:cliente')

#--------------Views para Cliente--------------#

def listar_autor(request):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    autores = Autores.objects.all() #Traemos TODOS los datos de la tabla autores 

    if busqueda: #Preguntando si busqueda está llena 
        autores = Autores.objects.filter(
            Q(id_autor__icontains = busqueda) |
            Q(apellidos__icontains = busqueda) | 
            Q(nombres__icontains = busqueda)
        )
    
    return render(request, 'autor.html', {'autores':autores})

#--------------Views para Autor--------------#

class AgregarAutor(CreateView):
    model = Autores
    form_class = AutorForm
    template_name = 'modals/autor/agregar_autor.html'
    success_url = reverse_lazy('libreria:autor')

class EditarAutor(UpdateView):
    model = Autores
    template_name = 'modals/autor/editar_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libreria:autor')
   
class EliminarAutor(DeleteView):
    model = Autores
    template_name = 'modals/autor/eliminar_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libreria:autor')


#--------------Views para Categoria--------------# 

def listar_categoria(request):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    categoria = Categorias.objects.all() #Traemos TODOS los datos de la tabla autores 

    if busqueda: #Preguntando si busqueda está llena 
        categoria = Categorias.objects.filter(
            Q(id_categoria__icontains = busqueda) |
            Q(categoria__icontains = busqueda)
        )
    
    return render(request, 'categoria.html', {'categorias':categoria})

class AgregarCategoria(CreateView):
    model = Categorias 
    template_name = 'modals/categoria/agregar_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('libreria:categoria')

class EditarCategoria(UpdateView):
    model = Categorias 
    template_name = 'modals/categoria/editar_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('libreria:categoria')

class EliminarCategoria(DeleteView):
    model = Categorias
    template_name = 'modals/categoria/eliminar_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('libreria:categoria')


#--------------Views para Libro--------------# 

def listar_libro(request):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    libro = Libros.objects.all() #Traemos TODOS los datos de la tabla autores 

    if busqueda: #Preguntando si busqueda está llena 
        libro = Libros.objects.filter(
            Q(isbn__icontains = busqueda) |
            Q(titulo__icontains = busqueda) |
            Q(fecha_pub__icontains = busqueda) |
            Q(precio__icontains = busqueda)
        )
    
    return render(request, 'libro.html', {'libros':libro})  

class AgregarLibro(CreateView):
    model = Libros
    form_class = LibroForm
    template_name = 'modals/libro/agregar_libro.html'
    success_url = reverse_lazy('libreria:libro')

class EditarLibro(UpdateView):
    model = Libros
    form_class= LibroForm
    template_name = 'modals/libro/editar_libro.html'
    success_url = reverse_lazy('libreria:libro')

class EliminarLibro(DeleteView):
    model = Libros
    template_name = 'modals/libro/eliminar_libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('libreria:libro') 

def listar_pedido(request):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    pedido = PedidosCliente.objects.all() #Traemos TODOS los datos de la tabla autores 

    if busqueda: #Preguntando si busqueda está llena 
        pedido = PedidosCliente.objects.filter(
            Q(nro_pedido__icontains = busqueda) |
            Q(id_cliente__exact = busqueda) |
            Q(isbn__exact = busqueda) |
            Q(valor__icontains = busqueda) 
        )
    
    return render(request, 'pedidos.html', {'pedidos':pedido})  


def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active():
        auth.login(request, user)
        return HttpResponseRedirect('/account/loggedin')
    else:
        return HttpResponseRedirect('/account/invalid')



def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect('/account/loggedin')