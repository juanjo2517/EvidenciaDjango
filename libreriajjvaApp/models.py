# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=25)
    nombres = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'autores'
    
    def __str__(self):
        return '{} - {} - {}'.format(
            self.id_autor,
            self.nombres,
            self.apellidos
        )
    


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'categorias'
    
    def __str__(self):
      return '{} - {}'.format(
            self.id_categoria,
            self.categoria
        )


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=12)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    correo_electronico = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
            self.identificacion,
            self.nombres,
            self.apellidos,
            self.telefono,
            self.correo_electronico
        )

class LibroPorAutor(models.Model):
    id_autor = models.OneToOneField(Autores, models.DO_NOTHING, db_column='id_autor', primary_key=True)
    isbn = models.ForeignKey('Libros', models.DO_NOTHING, db_column='isbn')

    class Meta:
        managed = False
        db_table = 'libro_por_autor'
        unique_together = (('id_autor', 'isbn'),)

    def __str__(self):
        return '{} - {}'.format(
            self.id_autor,
            self.isbn
        )


class Libros(models.Model):
    isbn = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=128)
    fecha_pub = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='categoria')
    precio = models.IntegerField()
    portada = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libros'

    def __str__(self):
        return '{} - {} - {}'.format(
            self.isbn,
            self.titulo,
            self.precio
        )


class PedidosCliente(models.Model):
    nro_pedido = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    isbn = models.ForeignKey(Libros, models.DO_NOTHING, db_column='isbn')
    fecha_pedido = models.DateField()
    cantidad = models.IntegerField()
    valor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedidos_cliente'

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
            self.nro_pedido,
            self.id_cliente,
            self.isbn,
            self.cantidad,
            self.valor
        )
