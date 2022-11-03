from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from WebFinal.forms import Formulario_cliente
from WebFinal.models import *
from WebFinal.forms import *
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def form_cliente(request):

    
    
    if request.method == 'POST':

        add_cliente = Formulario_cliente(request.POST)
        
        if add_cliente.is_valid():

            datos = add_cliente.cleaned_data
            nuevo_cliente = Cliente(nombre=datos['nombre'], apellido=datos['apellido'], telefono=datos['telefono'], direccion=['direccion'])
            nuevo_cliente.save()
            return HttpResponseRedirect('/form_cliente/')
        
    else:
        add_cliente = Formulario_cliente()

    return render(request, 'form_cliente.html', {'add_cliente': add_cliente})


def form_empleado(request):
    #cuerpo 

    return render(request, 'form_empleado')


def form_productos(request):
    #cuerpo 

    return render(request, 'form_productos')



def form_proveedores(request):
   #cuerpo 

    return render(request, 'form_proveedores')

