from django.contrib import admin
from .models import Autores, Categorias, Cliente, LibroPorAutor, Libros, PedidosCliente

# Register your models here.

admin.site.register(Autores)
admin.site.register(Categorias)
admin.site.register(Cliente)
admin.site.register(LibroPorAutor)
admin.site.register(Libros)
admin.site.register(PedidosCliente)

