import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Categoria

# Create your tests here.

class CategoriaModelTest(TestCase):

    def setUp(self):
        nombre1 = Categoria.objects.create(nombre = "Pediatria")

    def prueba_clase_categoria(self):
        self.assertIs(nombre1, False)
