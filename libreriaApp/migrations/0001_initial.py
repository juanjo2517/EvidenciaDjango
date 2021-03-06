# Generated by Django 3.0.6 on 2020-06-21 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=25)),
                ('nombres', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['id_autor'],
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['id_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=128)),
                ('fecha_pub', models.DateField(blank=True, null=True)),
                ('precio', models.IntegerField()),
                ('portada', models.ImageField(blank=True, default='', max_length=200, null=True, upload_to='portada/', verbose_name='Imagen de Portada')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreriaApp.Categorias')),
                ('id_autor', models.ManyToManyField(to='libreriaApp.Autores')),
            ],
            options={
                'ordering': ['isbn'],
            },
        ),
        migrations.CreateModel(
            name='PedidosCliente',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateField(auto_now=True)),
                ('cantidad', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreriaApp.Libros')),
            ],
            options={
                'ordering': ['id_pedido'],
            },
        ),
    ]
