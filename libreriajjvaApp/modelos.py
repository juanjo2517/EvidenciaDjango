from django.db import models

# Create your models here.

class Categoria(models.Model):

    id = models.AutoField(primary_key=True)
    categoria = models.CharField('Categoría', max_length=40)

    def __str__(self):
        listaCategoria = []
        listaCategoria.append(self.id)
        listaCategoria.append(self.categoria)

        return str(listaCategoria)

class Autor(models.Model):

    id = models.AutoField(primary_key=True)
    apellidos = models.CharField('Apellidos', max_length=25)
    nombres = models.CharField('Nombres', max_length=25)

    def __str__(self):
        listaAutor = []
        listaAutor.append(self.id)
        listaAutor.append(self.apellidos)
        listaAutor.append(self.nombres)

        return  str(listaAutor)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    identificacion = models.CharField('Número de Identificación', max_length=12)
    nombres = models.CharField('Nombres',max_length=25)
    apellidos = models.CharField('Apellidos',max_length=25)
    telefono = models.CharField('Teléfono',max_length=25)
    direccion = models.CharField('Dirección',max_length=128, null=True)
    correo_electronico = models.EmailField('Correo Electrónico', max_length=128)

    def __str__(self):
        
        listaCliente = []
        listaCliente.append(self.id_cliente)
        listaCliente.append(self.identificacion)
        listaCliente.append(self.nombres)
        listaCliente.append(self.apellidos)
        listaCliente.append(self.telefono)
        listaCliente.append(self.direccion)
        listaCliente.append(self.correo_electronico)

        return str(listaCliente)

class Libro(models.Model):
    isbn = models.IntegerField(primary_key=True)
    titulo = models.CharField('Título', max_length=128)
    fecha_pub = models.DateField()
    categoria = models.ForeignKey(Categoria, models.CASCADE)
    precio = models.IntegerField()
    portada = models.ImageField(null=True)

    def __str__(self):
        
        listaLibro = []
        listaLibro.append(self.isbn)
        listaLibro.append(self.titulo)
        listaLibro.append(self.fecha_pub)
        listaLibro.append(self.categoria)
        listaLibro.append(self.precio)

        return str(listaLibro)

class PedidosCliente(models.Model):

    id = models.AutoField(primary_key=True)
    nro_pedido = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.CASCADE)
    isbn = models.ForeignKey(Libro, models.CASCADE)
    fecha_pedido = models.DateField()
    cantidad = models.IntegerField(default=1)
    valor = models.IntegerField()

    def __str__(self):
        
        listaPedidosCliete = []
        listaPedidosCliete.append(self.id)
        listaPedidosCliete.append(self.nro_pedido)
        listaPedidosCliete.append(self.id_cliente)
        listaPedidosCliete.append(self.isbn)
        listaPedidosCliete.append(self.fecha_pedido)
        listaPedidosCliete.append(self.cantidad)
        listaPedidosCliete.append(self.valor)

        return str(listaPedidosCliete)

class LibroPorAutor(models.Model):
    id_autor = models.IntegerField(primary_key=True) 
    models.ForeignKey(Autor, models.CASCADE)
    isbn = models.IntegerField(primary_key=True)
    models.ForeignKey(Libro, models.CASCADE)