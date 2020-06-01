from django import forms
from .models import Cliente, Autores, Categorias, Libros
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['identificacion','nombres','apellidos','telefono','direccion','correo_electronico']

        widgets = {
            'identificacion': forms.NumberInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese N° de Identificación'
                }
            ), 
            'nombres': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre'
                }
            ), 
            'apellidos': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Apellido'
                }
            ), 
            'telefono': forms.NumberInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese N° de Teléfono'
                }
            ), 
            'direccion': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Dirección'
                }
            ), 
            'correo_electronico': forms.EmailInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Correo Electrónico'
                }
            )
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['nombres','apellidos']

        widgets = {
            'nombres': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre del Autor'
                }
            ), 
            'apellidos': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Apellido del Autor'
                }
            )
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['categoria']

        widgets = {
            'categoria': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Categoría'
                }
            )
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['isbn','titulo', 'fecha_pub','categoria', 'id_autor', 'precio','portada']
        
        años = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
          '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
          '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
          '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
          '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019','2020')

        widgets = {
            'isbn': forms.NumberInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese ISBN'
                }
            ),
            'titulo': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Título'
                }
            ),
            'fecha_pub': forms.SelectDateWidget(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Fecha de Publicación'
                },
                years=años, 
                
            ),
            'categoria': forms.Select(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Categoría'
                }
            ),
            'id_autor': forms.Select(
                attrs= {
                    'class': 'form-control'
                }
            ),
            'precio': forms.NumberInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Precio'
                }
            ),
            'portada': forms.FileInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Imagen de Portada'
                }
            )
        }
