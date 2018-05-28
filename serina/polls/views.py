from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormCategoria
from .models import Categoria
# Create your views here.
def index(request):
    return render(request, 'serina_views/index.html')

def prueba(request):
    return render(request, 'serina_views/prueba.html')

def form_categoria(request):
    return render(request, 'serina_views/formTratamiento.html')

def add_categoria(request):
    form = FormCategoria(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        categoria = form_data.get("nombre")
        obj = Categoria.objects.create(nombre = categoria)
    context = {'form': form}
    return render(request, "serina_views/prueba.html", context)
