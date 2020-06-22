from django.shortcuts import render, redirect
from django.contrib import auth 
from django.views.defaults import page_not_found
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Autores, Categorias, Libros, PedidosCliente
from .forms import AutorForm, CategoriaForm, LibroForm, PedidoClienteForm

# Create your views here.

def pagina_404(request):
    return render(request, '404.html')


def index(request):
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id)
    
    return render(request, 'index.html', {'carrito':carrito}) #index.html es el template


#--------------Views para Cliente--------------#

""" def listar_cliente(request):
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
 """
#--------------Views para Cliente--------------#

def listar_autor(request):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    autores = Autores.objects.all()
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id) #Traemos TODOS los datos de la tabla autores 

   
    if busqueda: #Preguntando si busqueda está llena 
        autores = Autores.objects.filter(
            Q(id_autor__icontains = busqueda) |
            Q(apellidos__icontains = busqueda) | 
            Q(nombres__icontains = busqueda)
        )
    datos = {
        'autores': autores,
        'carrito': carrito
    }
    return render(request, 'autor.html', datos)

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
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id)

    if busqueda: #Preguntando si busqueda está llena 
        categoria = Categorias.objects.filter(
            Q(id_categoria__icontains = busqueda) |
            Q(categoria__icontains = busqueda)
        )
    datos = {
        'categorias':categoria,
        'carrito': carrito
    }
    
    return render(request, 'categoria.html', datos)

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
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id)

    if busqueda: #Preguntando si busqueda está llena 
        libro = Libros.objects.filter(
            Q(isbn__icontains = busqueda) |
            Q(titulo__icontains = busqueda) |
            Q(fecha_pub__icontains = busqueda) |
            Q(precio__icontains = busqueda)
        )
    datos = {
        'libros': libro,
        'carrito': carrito 
    }
    
    return render(request, 'libro.html', datos)  

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

def listar_pedido(request, user_id):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    pedido = PedidosCliente.objects.filter(id_cliente = user_id) #Traemos TODOS los datos de la tabla autores 
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id)

    if busqueda: #Preguntando si busqueda está llena 
        pedido = PedidosCliente.objects.filter(
            Q(nro_pedido__icontains = busqueda) |
            Q(id_cliente__exact = busqueda) |
            Q(isbn__exact = busqueda) |
            Q(valor__icontains = busqueda),
            id_cliente = user_id 
        )
    
    datos = {
        'pedidos':pedido,
        'carrito': carrito
    }
    
    return render(request, 'pedidos.html', datos)  

class AgregarPedidoCliente(CreateView):
    model = PedidosCliente
    form_class = PedidoClienteForm
    template_name = 'modals/pedido_cliente/agregar_pedido_cliente.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            isbn_libro = form.cleaned_data.get('isbn').isbn
            cantidad = int(form.cleaned_data.get('cantidad'))
            precio_libro = int(Libros.objects.get(isbn = isbn_libro).precio)
            valor_pedido = cantidad*precio_libro

            nuevo_pedido = PedidosCliente(
                id_cliente = form.cleaned_data.get('id_cliente'),
                isbn = form.cleaned_data.get('isbn'),
                cantidad = form.cleaned_data.get('cantidad'),
                valor = valor_pedido
            )

            nuevo_pedido.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, 'pedidos.html', {'form':form})


    


class EliminarPedido(DeleteView):
    model = PedidosCliente
    form_class = PedidoClienteForm
    template_name = 'modals/pedido_cliente/eliminar_pedido_cliente.html'
    success_url = reverse_lazy('libreria:pedidos_cliente')


def eliminar_pedido(request, id_pedido):
    pedido = PedidosCliente.objects.get(id_pedido = id_pedido)
    pedido.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

""" class EditarPedidoCliente(UpdateView):
    model = PedidosCliente
    form_class = PedidoClienteForm
    template_name = 'modals/pedido_cliente/editar_pedido_cliente.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            id_pedido = request.POST.get('id_pedido')
            pedido = PedidosCliente.objects.get(id_pedido = id_pedido)
            isbn_libro = request.POST.get('isbn') 
            cantidad = int(request.POST.get('cantidad'))
            precio_libro = int(Libros.objects.get(isbn = isbn_libro).precio)
            
            if pedido:
                pedido.isbn = form.cleaned_data.get('isbn')
                pedido.cantidad = cantidad
                pedido.valor = cantidad*precio_libro
                
                return redirect('libreria:pedidos_cliente')
            else: 
                return render(request, 'pedidos.html', {'form':'Error'}) 
        else: 
            return render(request, 'pedidos.html', {'form':'Error'})

 """

def detalle(request):
    return render(request, 'modals/libro/libro_detalle.html')
