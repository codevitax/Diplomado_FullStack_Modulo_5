from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria
from .models import Product
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ProductoSerializer, ContactSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hola mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de django")

def categorias(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get('nombre')
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    return render(request, "form_categorias.html", {
        "categorias": categorias
    })

def productoFormView(request):
    form = ProductForm()
    producto = None
    id_producto = request.GET.get('id')
    if id_producto:
        producto = get_object_or_404(Product, id=id_producto)
        form = ProductForm(request.POST, instance=producto)

    if request.method == "POST":
        if producto:
            form = ProductForm(request.POST, instance=producto)
        else:
            form = ProductForm(request.POST)  

    if form.is_valid():
        form.save()
        
    return render(request, "form_productos.html", {
        "form": form
    })

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(["GET"])
def categoria_count(request):
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse({
            "cantidad": cantidad
            },
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def productos_en_unidades(request):
    """
    Esto solo muestra productos por unidades
    """
    try:
        productos = Product.objects.filter(unidades="u")
        return JsonResponse(
            ProductoSerializer(productos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["POST"])
def enviar_mensaje(request):
    """
    HOLA POST
    """
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({"mensaje": "Mensaje enviado correctamente"}, status=200)
    else:
        return JsonResponse({"mensaje": cs.errors}, status=400)