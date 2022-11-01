from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from WebFinal.models import cliente
from WebFinal.forms import Formulario_cliente

# Create your views here.

def inicio(request):
    return render(request, 'I:/Python/Proyectos/ProyectoFinal/WebFinal/templates/inicio.html')

def form_cliente(request):

    print('method:', request.method)
    print('post: ', request.POST)
    
    if request.method == 'POST':
        add_cliente = Formulario_cliente(request.POST)
        print(add_cliente)
        if add_cliente.is_valid():
            datos = add_cliente.cleaned_data
            nuevo_cliente = cliente(nombre=datos['nombre'], apellido=datos['apellido'], telefono=datos['telefono'], direccion=['direccion'])
            nuevo_cliente.save()
            return redirect('form_cliente')
    else:
        add_cliente = Formulario_cliente()

    return render(request, 'form_cliente.html')
