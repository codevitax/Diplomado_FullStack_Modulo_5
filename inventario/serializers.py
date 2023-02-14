from rest_framework import serializers
from .models import Categoria
from .models import Product
from .validators import validar_nombre


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100, validators=[validar_nombre,])
    body = serializers.CharField(max_length=255)