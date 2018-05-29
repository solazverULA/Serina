from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormCategoria
from .models import Categoria

# Create your views here.
def index(request):
    return render(request, 'serina_views/index.html')

def ver_categ(request):
    return render(request, 'serina_views/ver_categ.html')

def form_categoria(request):
    return render(request, 'serina_views/formTratamiento.html')

def add_categoria(request):

    categoria = request.POST['categoria']
    context = {'categoria': categoria}
    db_o = Categoria(nombre=categoria)
    db_o.save()
    return render(request, "serina_views/ver_categ.html", context)

def add_cita(request):

    fecha = request.POST['fecha']
    nota = request.POST['nota']
    context = {'fecha': fecha, 'nota': nota}
    db_fecha = Cita(fecha = fecha)
    db_fecha.save()
    db_nota = Cita(nota = nota)
    db_nota.save()
    return render(request, "serina_views/ver_categ.html", contex)


def add_indicaciones(request):

    #medicina = request.POST['medicina']
    #context = {'medicina': medicina}

    #db_medicina = Medicina(nombre = medicina)

    return render(request, "serina_views/form_indicaciones.html")



def consultar_categ(resquest):
    categoria = Categoria.objects.all()
    return render(request, "serina_views/ver_categ.html", {'categoria': categoria})
