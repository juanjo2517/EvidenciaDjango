from django.urls import path
from django.conf.urls import handler404
from django.contrib.auth.decorators import login_required
from .views import index, listar_pedido, pagina_404, detalle
from .views import listar_cliente, listar_autor, listar_categoria
from .views import listar_libro, AgregarCliente, EditarCliente, EliminarCliente, AgregarAutor
from .views import EditarAutor, EliminarAutor, AgregarCategoria, EditarCategoria, EliminarCategoria
from .views import AgregarLibro, EditarLibro, EliminarLibro


#handler404 = pagina_404

urlpatterns = [
    path('', index, name='index'),
    path('pedidos_cliente', login_required(listar_pedido), name='pedidos_cliente'),
    #Clientes
    path('cliente/', login_required(listar_cliente), name='cliente'),
    path('agregar_cliente/', login_required(AgregarCliente.as_view()), name='agregar_cliente'),
    path('editar_cliente/<int:pk>', login_required(EditarCliente.as_view()), name='editar_cliente'),
    path('eliminar_cliente/<int:pk>', login_required(EliminarCliente.as_view()), name='eliminar_cliente'),
    #Autores
    path('autor/', login_required(listar_autor), name='autor'),
    path('agregar_autor/', login_required(AgregarAutor.as_view()), name='agregar_autor'),
    path('editar_autor/<int:pk>', login_required(EditarAutor.as_view()), name='editar_autor'),
    path('eliminar_autor/<int:pk>', login_required(EliminarAutor.as_view()), name='eliminar_autor'),

    #Categoria
    path('categoria/', login_required(listar_categoria), name='categoria'),
    path('agregar_categoria/', login_required(AgregarCategoria.as_view()), name='agregar_categoria'),
    path('editar_categoria/<int:pk>', login_required(EditarCategoria.as_view()), name='editar_categoria'),
    path('eliminar_categoria/<int:pk>', login_required(EliminarCategoria.as_view()), name='eliminar_categoria'),

    #Libro
    path('libro/', login_required(listar_libro), name='libro'),
    path('agregar_libro/', login_required(AgregarLibro.as_view()), name='agregar_libro'),
    path('editar_libro/<int:pk>', login_required(EditarLibro.as_view()), name='editar_libro'),
    path('eliminar_libro/<int:pk>', login_required(EliminarLibro.as_view()), name='eliminar_libro'),
    path('detalle_libro/', login_required(detalle), name='libro_detalle'),

]
