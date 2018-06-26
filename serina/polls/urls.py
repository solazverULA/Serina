from django.urls import path, include, reverse

#se importan todas las urls de la vista de polls
from . import views

#app_name = 'polls'
urlpatterns = [
    path('index/', views.index, name ='index'),
    path('formulario/', views.view_categoria, name = 'view_categoria'),
    path('formulario/categoria', views.show_categoria, name = 'show_categoria'),
    path('formulario/addcategoria', views.add_categoria, name = 'add_categoria'),
    path('formulario/deletecategoria', views.delete_categoria, name = 'delete_categoria'),
    path('formulario/addcita', views.add_cita, name = 'add_cita'),
    path('formulario/deletecita', views.delete_cita, name = 'delete_cita'),
    path('formulario/indicaciones', views.show_indicaciones, name = 'show_indicaciones'),
    path('formulario/addindicaciones', views.add_indicaciones, name = 'add_indicaciones'),
    path('index/login', views.show_login, name = 'show_login'),
    path('index/signup', views.show_sign_up, name = 'show_sign_up'),
    path('index/addsingup', views.add_sing_up, name = 'add_sing_up'),
    path('index/addsingin', views.add_sing_in, name = 'add_sing_in'),
    path('formulario/addtratamiento', views.add_tratamiento, name = 'add_tratamiento'),
    path('formulario/tratamiento', views.show_tratamiento, name = 'show_tratamiento'),
    path('formulario/datostratamiento', views.view_tratamiento, name = 'view_tratamiento'),
    path('formulario/addinformacion', views.add_informacion, name = 'add_informacion'),
    path('formulario/addmedicina', views.add_medicina, name = 'add_medicina'),
]
