from django.urls import path, re_path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import (listar_usuario_cliente, 
RegistrarUsuario, AgregarFotoPerfil, EliminarCliente, EditarCliente)

urlpatterns = [
    path('', RegistrarUsuario.as_view(), name='registro'),
    path('registrar_usuario/', RegistrarUsuario.as_view(template_name = 'modals/cliente/agregar_cliente.html', 
    success_url = reverse_lazy('usuario:usuario_cliente')), name='registro_usuario'),
    path('clientes/', listar_usuario_cliente, name = 'listar_cliente'),    
    path('usuario_cliente/', listar_usuario_cliente, name = 'usuario_cliente'),
    path('agregar_foto/<int:pk>', login_required(AgregarFotoPerfil.as_view()), name='agregar_foto'),
    path('editar_cliente/<int:pk>', login_required(EditarCliente.as_view()), name='editar_cliente'),
    path('eliminar_cliente/<int:pk>', login_required(EliminarCliente.as_view()), name='eliminar_cliente'),
]