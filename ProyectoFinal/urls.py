"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WebFinal.forms import Formulario_empleado
from WebFinal.views import form_cliente
from WebFinal.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('form_cliente/', form_cliente, name='form_cliente'),
    path('form_empleado/', form_empleado, name='form_empleado'),
    path('form_productos/', form_productos, name='form_productos'),
    path('form_proveedores/', form_proveedores, name='form_proveedores'),
    path('cliente_creado/', form_cliente, name='form_cliente'),
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('borracliente/<int:id>', borracliente, name='borracliente'),
    path('editarcliente/<int:id>', editar_cliente, name='editarcliente')

]
