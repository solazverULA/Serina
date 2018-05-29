from django.urls import path, include, reverse

#se importan todas las urls de la vista de polls
from . import views

#app_name = 'polls'
urlpatterns = [
    path('index/', views.index, name ='index'),
    path('formulario/', views.form_categoria, name = 'form_categoria'),
    path('formulario/verCateg', views.ver_categ, name = 'ver_categ'),
    path('formulario/addcategoria', views.add_categoria, name = 'add_categoria'),
    path('formulario/addcita', views.add_cita, name = 'add_cita'),
    path('formulario/consultarcateg', views.consultar_categ, name = 'cosultar_categ'),
    path('formulario/addIndicaciones', views.add_indicaciones, name = 'add_indicaciones'),
]
