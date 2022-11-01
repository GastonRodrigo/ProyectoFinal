from django import forms

class Formulario_cliente(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.CharField(max_length=30)
    direccion = forms.CharField(max_length=60)



