from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, '/Users/harkonen/Desktop/ProyectoFinal/ProyectoFinal/WebFinal/templates/inicio.html')