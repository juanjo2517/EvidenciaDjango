from django.urls import path
from .views import index, listar_libro_por_autor, listar_pedido
from .views import listar_cliente, listar_autor, listar_categoria
from .views import listar_libro, AgregarCliente, EditarCliente, EliminarCliente, AgregarAutor
from .views import EditarAutor, EliminarAutor, AgregarCategoria, EditarCategoria, EliminarCategoria
from .views import AgregarLibro, EditarLibro, EliminarLibro, AgregarLibroPorAutor, EditarLibroPorAutor

urlpatterns = [
    path('', index, name='index'),
    path('pedidos_cliente', listar_pedido, name='pedidos_cliente'),
    #Clientes
    path('cliente/', listar_cliente, name='cliente'),
    path('agregar_cliente/', AgregarCliente.as_view(), name='agregar_cliente'),
    path('editar_cliente/<int:pk>', EditarCliente.as_view(), name='editar_cliente'),
    path('eliminar_cliente/<int:pk>', EliminarCliente.as_view(), name='eliminar_cliente'),
    #Autores
    path('autor/', listar_autor, name='autor'),
    path('agregar_autor/', AgregarAutor.as_view(), name='agregar_autor'),
    path('editar_autor/<int:pk>', EditarAutor.as_view(), name='editar_autor'),
    path('eliminar_autor/<int:pk>', EliminarAutor.as_view(), name='eliminar_autor'),

    #Categoria
    path('categoria/', listar_categoria, name='categoria'),
    path('agregar_categoria/', AgregarCategoria.as_view(), name='agregar_categoria'),
    path('editar_categoria/<int:pk>', EditarCategoria.as_view(), name='editar_categoria'),
    path('eliminar_categoria/<int:pk>', EliminarCategoria.as_view(), name='eliminar_categoria'),

    #Libro
    path('libro/', listar_libro, name='libro'),
    path('agregar_libro/', AgregarLibro.as_view(), name='agregar_libro'),
    path('editar_libro/<int:pk>', EditarLibro.as_view(), name='editar_libro'),
    path('eliminar_libro/<int:pk>', EliminarLibro.as_view(), name='eliminar_libro'),

    #LibroPorAutor
    path('libro_por_autor/', listar_libro_por_autor, name='libro_por_autor'),
    path('agregar_libro_autor/', AgregarLibroPorAutor.as_view(), name='agregar_libro_autor'),
    path('editar_libro_autor/<int:pk>', EditarLibroPorAutor.as_view(), name='editar_libro_autor'),
]
