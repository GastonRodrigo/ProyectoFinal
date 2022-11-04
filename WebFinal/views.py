from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.test import Client
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from WebFinal.forms import Formulario_cliente
from WebFinal.models import *
from WebFinal.forms import *
# Create your views here.

def inicio(request):

    return render(request, 'inicio2.html')

# def form_cliente(request):

#     #CREATE
    
#     if request.method == 'POST':

#         add_cliente = Formulario_cliente(request.POST)
        
#         if add_cliente.is_valid():

#             datos = add_cliente.cleaned_data
#             nuevo_cliente = Cliente(nombre=datos['nombre'], apellido=datos['apellido'], telefono=datos['telefono'], direccion=datos['direccion'])
#             nuevo_cliente.save()
#             return render(request, 'cliente_creado.html', {'mensaje':'Cliente creado con exito.'})
        
#     else:
#         add_cliente = Formulario_cliente()

#     return render(request, 'form_cliente.html', {'add_cliente': add_cliente})


class CrearCliente(CreateView):

    model = Cliente
    form_class = Formulario_cliente
    template_name = 'form_cliente.html'
    success_url = '/WebFinal/crear_exito/'


    #READ
# def lista_clientes(request):

#     clientes = Cliente.objects.all()

#     return render(request, "lista_clientes.html", {"clientes": clientes})

def creado_con_exito(request):

    return render(request,'crear_exito.html')

class Mostrar_clientes(ListView):

    model = Cliente
    template_name = "lista_clientes.html"
    context_object_name = "clientes"
    #EDIT

def borracliente(request, id):

    if request.method == 'POST':

        cliente = Cliente.objects.get(id=id)
        cliente.delete()

        clientes = Cliente.objects.all()

        return render(request, "lista_clientes.html", {"clientes": clientes})  

class Detalle_cliente(DetailView):

    model = Cliente
    template_name = "detalle_cliente.html"
    context_object_name = "cliente"

class EditarCliente(UpdateView):

    model = Cliente
    template_name = "edita_cliente.html"
    fields = ('__all__')
    success_url = '/WebFinal/exito_update/'

# def editar_cliente(request, id):

#     print('method:', request.method)
#     print('post: ', request.POST)

#     cliente = Cliente.objects.get(id=id)

#     if request.method == 'POST':

#         cliente_edit = Formulario_cliente(request.POST)

#         if cliente_edit.is_valid():

#             datos = cliente_edit.cleaned_data

#             cliente.nombre = datos["nombre"]
#             cliente.apellido = datos["apellido"]
#             cliente.telefono = datos["telefono"]
#             cliente.direccion = datos["direccion"]

#             cliente.save()

#             return HttpResponseRedirect('/WebFinal/lista_clientes/')
    
#     else:

#         cliente_edit = Formulario_cliente(initial={
#             "nombre": cliente.nombre,
#             "apellido": cliente.apellido,
#             "telefono": cliente.telefono,
#             "direccion": cliente.direccion,
#         })

#         return render(request, "editarcliente.html", {"cliente_edit": cliente_edit, "id": cliente.id})


def form_empleado(request):
    #cuerpo 

    return render(request, 'form_empleado')


def form_productos(request):
    #cuerpo 

    return render(request, 'form_productos')



def form_proveedores(request):
   #cuerpo 

    return render(request, 'form_proveedores')

