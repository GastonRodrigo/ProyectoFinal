from django.urls import path
from .views import *


urlpatterns = [
    path('inicio2/', inicio, name='inicio2'),
    path('form_cliente/', CrearCliente.as_view(), name='form_cliente'),
    path('form_empleado/', form_empleado, name='form_empleado'),
    path('form_productos/', form_productos, name='form_productos'),
    path('form_proveedores/', form_proveedores, name='form_proveedores'),
    #path('cliente_creado/', form_cliente, name='clientecreado'),
    path('lista_clientes/', Mostrar_clientes.as_view(), name='lista_clientes'),
    path('borra_cliente/<pk>', Borracliente.as_view(), name='borracliente'),
    #path('editar-cliente/<int:id>', editar_cliente, name='editarcliente'),
    path('crear_exito/', creado_con_exito, name='crear_exito'),
    path('detalle_cliente/<pk>', Detalle_cliente.as_view(), name='detalle_cliente'),
    path('clienteupdate/<pk>', EditarCliente.as_view(), name='clienteupdate'),
    path('crear_empleado/', Empleados.as_view(), name='crea_empleado'),
    path('exito_empleado/',empleado_creado,name='exito_empleado'),

]
