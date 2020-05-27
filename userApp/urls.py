from django.urls import path, re_path
from .views import RegistrarUsuario, AgregarFotoPerfil

urlpatterns = [
    path('', RegistrarUsuario.as_view(), name='registro_usuario'),
    path('agregar_foto/<int:pk>', AgregarFotoPerfil.as_view(), name='agregar_foto'),
]