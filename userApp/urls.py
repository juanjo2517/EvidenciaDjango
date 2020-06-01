from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import RegistrarUsuario, AgregarFotoPerfil

urlpatterns = [
    path('', RegistrarUsuario.as_view(), name='registro_usuario'),
    path('agregar_foto/<int:pk>', login_required(AgregarFotoPerfil.as_view()), name='agregar_foto'),
]