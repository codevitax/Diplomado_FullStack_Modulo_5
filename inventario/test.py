from django.test import TestCase
from .models import Categoria
from django.core.exceptions import ValidationError


class TestCategorias(TestCase):
    # def test_grabacion(self): 
    #     q = Categoria(nombre='Bebidas')
    #     q.save()
    #     self.assertEqual(Categoria.objects.count(),1)

    def test_grabacion(self):
        # q = Categoria(nombre='Bebidas')
        # q.save()
        q = Categoria.objects.create(nombre='No permitido')
        self.assertRaises(ValidationError, q.full_clean)
        # self.assertEqual(Categoria.objects.count(),1)