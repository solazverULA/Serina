from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormCategoria, FormUsuario
from .models import Categoria
from .models import Cita
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'serina_views/index.html')

def form_categoria(request):
    return render(request, 'serina_views/ver_categ.html')

def add_categoria(request):

    categoria = request.POST['categoria']
    context = {'categoria': categoria}
    db_o = Categoria(nombre=categoria)
    db_o.save()
    return redirect('ver_categ')


def add_cita(request):
    categoria = request.POST['categ']
    fecha = request.POST['fechaa']
    nota = request.POST['notaa']

    email = Usuario.objects.get(pk ='kathesm903@gmail.com')

    id_categ = Categoria.objects.get(pk = categoria)

    cita = Cita(fecha = fecha, nota = nota, email_usuario = email, id_categoria = id_categ)
    cita.save()

    return redirect('ver_categ')

def ver_categ(request):
    categoria = Categoria.objects.all()
    cita = Cita.objects.all()
    context = {'categoria': categoria, 'cita': cita}
    return render(request, 'serina_views/ver_categ.html', context)

def add_indicaciones(request):

    #medicina = request.POST['medicina']
    #context = {'medicina': medicina}

    #db_medicina = Medicina(nombre = medicina)

    return render(request, "serina_views/form_indicaciones.html")

def ver_tratamiento(request):
    return render(request, "serina_views/ver_tratamiento.html")

def add_informacion(request):
    return render(request, "serina_views/form_informacion.html")

def mostrar_login(request):
    return render(request, "serina_views/sign_in.html" )

def mostrar_sign_up(request):
    return render(request, "serina_views/sign_up.html")

def add_sing_up(request):
    email = request.POST['cuenta']
    password = request.POST['password']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    ci = request.POST['cedula']
    nacimiento = request.POST['fecha_nacimiento']
    altura = request.POST['altura']
    db_object = Usuario(email = email, contrasena = password, nombre = nombre, apellido = apellido, ci = ci, fecha_nacimiento =nacimiento, altura = altura)
    db_object.save()
    return render(request, "serina_views/index.html")

def sing_in(request):
    email = request.POST['lemail']
    password = request.POST['lpassword']

    try:
        usuario = Usuario.objects.get(pk=email)
    except Usuario.DoesNotExist:
        raise Http404("User does not exist")

    if(usuario.contrasena == password):
        return HttpResponse('<h1>User login</h1>')
    else:
        return HttpResponse('<h1>User logout</h1>')
