from django.db import models
from .validators import validar_par
from django.core.validators import EmailValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

# Esto es para que en el admin muestro los objetos con sus nombres especificos
    def __str__(self):
        return self.nombre

class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades',
    KG = 'kg', 'Kilogramos',

class Product(models.Model):
    nombre = models.CharField(max_length=255, validators=[EmailValidator("el email no es valido")])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_par])
    unidades = models.CharField(
        max_length = 2,
        choices = ProductUnits.choices,
        default = ProductUnits.UNITS
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.precio}"
    