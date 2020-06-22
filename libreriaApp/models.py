
from django.db import models
from userApp.models import UsuarioCliente

class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=25, blank = False, null = False)
    nombres = models.CharField(max_length=25, blank = False, null = False)

    class Meta:
        ordering = ['id_autor']

    def __str__(self):
        return self.nombres +" "+ self.apellidos



class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=40, blank = False, null = False)

    class Meta:
        ordering = ['id_categoria']

    def __str__(self):
      return '{} - {}'.format(
            self.id_categoria,
            self.categoria
        )

class Libros(models.Model):
    isbn = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=128, blank = False, null = False)
    fecha_pub = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
    precio = models.IntegerField()
    portada = models.ImageField('Imagen de Portada', upload_to='portada/', max_length=200, blank = True,null = True, default='')
    id_autor = models.ManyToManyField(Autores)
    
    class Meta:
        ordering = ['isbn']

    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.isbn,
            self.titulo,
            "$"+str(self.precio),
            self.portada
        )

class PedidosCliente(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(UsuarioCliente, on_delete = models.CASCADE)
    isbn = models.ForeignKey(Libros, on_delete = models.CASCADE)
    fecha_pedido = models.DateField(auto_now = True, auto_now_add = False)
    cantidad = models.IntegerField()
    valor = models.IntegerField()

    class Meta:
        ordering = ['id_pedido']

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
            self.id_pedido,
            self.id_cliente,
            self.isbn,
            self.cantidad,
            self.valor
        )

""" class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=12, blank = False, null = False)
    nombres = models.CharField(max_length=25, blank = False, null = False)
    apellidos = models.CharField(max_length=25, blank = False, null = False)
    telefono = models.CharField(max_length=12, blank = False, null = False)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    correo_electronico = models.CharField(max_length=128, blank = False, null = False)
    
    class Meta:
        ordering = ['id_cliente']

    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
            self.id_cliente,
            self.identificacion,
            self.nombres,
            self.apellidos,
            self.telefono,
            self.correo_electronico
        )
 """