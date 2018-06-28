import datetime
from django.test import TestCase
from django.utils import timezone


from django.test import Client

from django.contrib.auth.models import User
from .models import Usuario

from .models import Categoria
from .models import Cita



# Create your tests here.

class CategoriaModelTests(TestCase):


    def setUp(self):

        self.user = User.objects.create_user('kathesm903@gmail.com',
                                             'kathesm903@gmail.com', 'qwerty1234')

        self.usuario = Usuario(email=self.user,
                               nombre = "Katherine",
                               apellido = "Andrade",
                               ci = "20199494",
                               fecha_nacimiento = "1990-10-24",
                               altura = 168)

        self.categoria = Categoria(nombre="Cardiología",
                                   email_usuario=self.user)


        self.cita = Cita(fecha='2018-07-29',
                         nota='Urgente',
                         email_usuario = self.user,
                         id_categoria = self.categoria)


        self.c = Client()


    def test_categoria_creation(self):
        """
        Prueba, se puede crear una categoria
        """
        self.assertEqual(self.categoria.nombre, "Cardiología")
        self.assertEqual(self.categoria.email_usuario, self.user)


    def test_categoria_listar_login(self):
        """
        Prueba, usuario logueado puede acceder a las categorias
        """
        self.c.login(username='kathesm903@gmail.com', password='qwerty1234')
        response = self.c.get('/serina/formulario/categoria')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content, '{}')


    def test_categoria_listar_no_login(self):
        """
        Prueba, usuario NO logueado puede acceder a las categorias, HTTP 403
        """
        response = self.c.get('/serina/formulario/categoria')
        self.assertEqual(response.status_code, 403)



    def test_cita_creation(self):
        """
        Prueba, se puede crear una cita, asociada a una categoria
        """
        self.assertEqual(self.cita.fecha, "2018-07-29")
        self.assertEqual(self.cita.nota, "Urgente")
        self.assertEqual(self.cita.email_usuario, self.user)
        self.assertEqual(self.cita.id_categoria, self.categoria)


    def test_cita_formulario_indicaciones_login(self):
        """
        Prueba, usuario logueado puede acceder a las categorias
        """
        self.c.login(username='kathesm903@gmail.com', password='qwerty1234')
        response = self.c.get('/serina/formulario/indicaciones?cita=1')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content, '{}')


    def test_cita_formulario_indicaciones_login(self):
        """
        Prueba, usuario NO logueado puede acceder a las citas, HTTP 403
        """
        response = self.c.get('/serina/formulario/indicaciones?cita=1')
        self.assertEqual(response.status_code, 403)
