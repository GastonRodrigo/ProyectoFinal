from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'I:/Python/Proyectos/ProyectoFinal/WebFinal/templates/inicio.html')