import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Categoria

# Create your tests here.

class CategoriaModelTest(TestCase):

    def setUp(self):
        Categoria.objects.create(nombre = "Pediatria")
        Categoria.objects.create(nombre = "ginecologia")

    def prueba_clase_categoria(self):
        nombre1 = Categoria.objects.get(pk = 1)
        nombre2 = Categoria.objects.get(pk = 2)

        prueba1 = nombre1.add_categoria()
        prueba2 = nombre2.add_categoria()
        self.assertFalse(prueba1)
        self.assertTrue(prueba2)
