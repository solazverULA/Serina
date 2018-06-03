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
    path('formulario/addIndicaciones', views.add_indicaciones, name = 'add_indicaciones'),
    path('index/login', views.mostrar_login, name = 'mostrar_login'),
    path('index/signup', views.mostrar_sign_up, name = 'mostrar_sign_up'),
    path('index/addsingup', views.add_sing_up, name = 'add_sing_up'),
    path('index/singin', views.sing_in, name = 'sing_in'),
    path('formulario/tratamiento', views.ver_tratamiento, name = 'ver_tratamiento'),
    path('formulario/addinformacion', views.add_informacion, name = 'add_informacion'),
]
