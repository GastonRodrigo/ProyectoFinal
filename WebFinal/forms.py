from django import forms
from .models import *

class Formulario_cliente(forms.ModelForm):

    # nombre = forms.CharField(max_length=30)
    # apellido = forms.CharField(max_length=30)
    # telefono = forms.CharField(max_length=30)
    # direccion = forms.CharField(max_length=60)
    class Meta:
        model = Cliente 
        fields = ("nombre","apellido", "telefono", "direccion")


class Formulario_empleado(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellida = forms.CharField(max_length=30)
    area = forms.CharField(max_length=30)
    cargo = forms.CharField(max_length=30)

class Formulario_proveedores(forms.Form):
    nombre = forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    telefono = forms.CharField(max_length=30)
    direccion = forms.CharField(max_length=60)

class Formulario_productos(forms.Form):
    modelo = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    medidas = forms.CharField(max_length=30)


