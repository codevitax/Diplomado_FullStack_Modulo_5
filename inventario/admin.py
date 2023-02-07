from django.contrib import admin
from .models import Categoria
from .models import Product

admin.site.register(Categoria)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "disponible",)
    ordering = ["precio", "nombre"]
    search_fields = ["nombre"]
    list_filter = ("disponible",)

admin.site.register(Product, ProductAdmin)
