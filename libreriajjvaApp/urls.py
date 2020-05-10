from django.urls import path
from .views import index, ListarCliente, ListarAutor, ListarCategoria, ListarLibro, ListarLibroPorAutor, ListarPedidoCliente


urlpatterns = [
    path('', index, name='index'),
    path('cliente/', ListarCliente.as_view(), name='cliente'),
    path('autor/', ListarAutor.as_view(), name='autor'),
    path('categoria/', ListarCategoria.as_view(), name='categoria'),
    path('libro/', ListarLibro.as_view(), name='libro'),
    path('libro_por_autor/', ListarLibroPorAutor.as_view(), name='libro_por_autor'),
    path('pedidos_cliente', ListarPedidoCliente.as_view(), name='pedidosCliente')
]

