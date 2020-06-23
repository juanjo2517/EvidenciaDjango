from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import UsuarioCliente
from .forms import FormUsuarioCliente, FormLogin, FormUsuarioFoto
# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = FormLogin
    success_url = reverse_lazy('libreria:index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self,form):
        login(self.request, form.get_user())
        return super(Login,self).form_valid(form)

def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


def listar_usuario_cliente(request):
    busqueda = request.POST.get("buscar")
    usuario_cliente = UsuarioCliente.objects.all()

    if busqueda:
        usuario_cliente = UsuarioCliente.objects.filter(
            Q(identificacion__icontains = busqueda) | 
            Q(nombre__icontains = busqueda) |
            Q(apellido__icontains = busqueda) |
            Q(email__icontains = busqueda)
        ).distinct()

    return render(request, 'clientes.html', {'usuario_cliente':usuario_cliente})


class RegistrarUsuario(CreateView):
    model = UsuarioCliente
    form_class = FormUsuarioCliente
    template_name = 'registro.html'
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = UsuarioCliente(
                identificacion = form.cleaned_data.get('identificacion'),
                nombre = form.cleaned_data.get('nombre'),
                apellido = form.cleaned_data.get('apellido'),
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                telefono = form.cleaned_data.get('telefono'),
                direccion = form.cleaned_data.get('direccion'),
                imagen = form.cleaned_data.get('imagen')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            
            if self.template_name == "registro.html":
                return render(request, 'registro_exitoso.html' )
            else:
                return redirect('usuario:listar_cliente')
        else:
            return render(request, self.template_name,{'form':form})

class AgregarFotoPerfil(UpdateView):
    model = UsuarioCliente
    form_class = FormUsuarioFoto
    template_name = 'modals/usuario/agregar_foto.html'
    success_url = reverse_lazy('libreria:index')

class EditarCliente(UpdateView):
    model = UsuarioCliente
    template_name = 'modals/cliente/editar_cliente.html'
    form_class = FormUsuarioCliente
    success_url = reverse_lazy('usuario:listar_cliente')
    

class EliminarCliente(DeleteView):
    model = UsuarioCliente
    template_name = 'modals/cliente/eliminar_cliente.html'
    form_class = FormUsuarioCliente
    success_url = reverse_lazy('libreria:cliente')