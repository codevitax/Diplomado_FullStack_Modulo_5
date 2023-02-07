from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria

def index(request):
    return HttpResponse("Hola mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de django")

def categorias(request):
    categorias = Categoria.objects.all()
    # filtro_nombre = request.GET.get('nombre')
    # nombre = Categoria.objects.filter(nombre__contains=filtro_nombre)
    return render(request, "categorias.html", {
        "categorias": categorias # puedo ponerle nombre si quiero 
    })