from django.urls import path
from .views import *


urlpatterns = [
    path('inicio2/', inicio, name='inicio2'),
    path('form_cliente/', CrearCliente.as_view(), name='form_cliente'),
    path('form_empleado/', form_empleado, name='form_empleado'),
    path('form_productos/', form_productos, name='form_productos'),
    path('form_proveedores/', form_proveedores, name='form_proveedores'),
    path('cliente_creado/', form_cliente, name='clientecreado'),
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('borracliente/<int:id>', borracliente, name='borracliente'),
    path('editar-cliente/<int:id>', editar_cliente, name='editarcliente'),
    path('crear_exito/', creado_con_exito, name='crear_exito')

]
