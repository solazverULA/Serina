from django.urls import path, include, reverse

#se importan todas las urls de la vista de polls
from . import views

#app_name = 'polls'
urlpatterns = [
    path('index/', views.index, name ='index'),
    path('formulario/', views.form_categoria, name = 'form_categoria'),
    path('formulario/prueba', views.prueba, name = 'prueba'),
    path('formulario/addcategoria', views.add_categoria, name = 'add_categoria'),
]
