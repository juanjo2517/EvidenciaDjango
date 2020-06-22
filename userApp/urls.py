from django.urls import path, re_path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import listar_usuario_cliente, RegistrarUsuario, AgregarFotoPerfil

urlpatterns = [
    path('', RegistrarUsuario.as_view(), name='registro'),
    path('registrar_usuario/', RegistrarUsuario.as_view(template_name = 'modals/cliente/agregar_cliente.html', 
    success_url = reverse_lazy('usuario:usuario_cliente')), name='registro_usuario'),
    
    path('usuario_cliente/', listar_usuario_cliente, name = 'usuario_cliente'),
    path('agregar_foto/<int:pk>', login_required(AgregarFotoPerfil.as_view()), name='agregar_foto'),
]