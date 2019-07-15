from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormCategoria, FormUsuario
from django.core.exceptions import PermissionDenied
from .models import Categoria
from .models import Cita
from .models import Usuario
from .models import Tratamiento
from .models import TipoMedicamento
from .models import Dosis
from .models import Medicina
from .models import Indicacion
from .models import TratamientoIndicacion

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
""" from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from datetime import date

import re """



# Create your views here.
def index(request):
    return render(request, 'serina_views/index.html')

def view_categoria(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    return render(request, 'serina_views/ver_categ.html')

def add_categoria(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    nombre = request.POST['categoria']
    categoria = nombre.lower()
    obj = Categoria.objects.all()
    for i in obj:
        nombres = i.nombre.lower()
        if(categoria == nombres):
            return HttpResponse("ERROR. ESTA AGREGANDO UNA CATEGORIA QUE YA EXISTE")

    email = User.objects.filter(email = request.session['user_email'])
    email_obj = User.objects.get(pk = email[0].id)



    db_o = Categoria(nombre=categoria, email_usuario=email_obj)
    db_o.save()


    return redirect('show_categoria')

def add_medicina(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    medicina = request.POST['medicina']
    tipo_medicamento = request.POST['tipo_medicamento']
    tipo_dosis = request.POST['tipo_dosis']
    concentracion = request.POST['concentracion']
    nombre = medicina.lower()

    context = {'medicina': nombre}
    obj_dosis = Dosis(tipo = tipo_dosis)
    obj_dosis.save()
    obj_tipo_medicamento = TipoMedicamento(nombre = tipo_medicamento)
    obj_tipo_medicamento.save()
    pk_dosis = Dosis(pk = tipo_dosis)
    pk_medicamento = TipoMedicamento(pk = tipo_medicamento)
    obj_medicina = Medicina(nombre = nombre, concentracion = concentracion, tipo_medicamento = pk_medicamento, tipo_dosis = pk_dosis)
    obj_medicina.save()


    return redirect('show_categoria')

def add_cita(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    categoria = request.POST['categ']
    fecha = request.POST['fechaa']
    nota = request.POST['notaa']

    email = User.objects.filter(email = request.session['user_email'])
    email_obj = User.objects.get(pk = email[0].id)


    id_categ = Categoria.objects.get(pk = categoria)
    cita = Cita(fecha = fecha, nota = nota, email_usuario = email_obj, id_categoria = id_categ)
    cita.save()
    return redirect('show_categoria')

def show_categoria(request):

    if not request.user.is_authenticated:
        raise PermissionDenied

    categoria = Categoria.objects.all()
    cita = Cita.objects.all
    tratamiento = Tratamiento.objects.all()
    context = {'categoria': categoria, 'cita': cita, 'tratamiento': tratamiento}
    return render(request, 'serina_views/ver_categ.html', context)

def delete_categoria(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    categoria = request.GET.get("categoria","")
    cita = Cita.objects.all()
    eliminar = Categoria.objects.get(pk = categoria)
    eliminar.delete()
    return redirect('show_categoria')

def delete_cita(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    cita = request.GET.get("cita", "")
    eliminar = Cita.objects.get(pk = cita)
    eliminar.delete()
    return redirect('show_categoria')

def show_tratamiento(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    cita = Cita.objects.all()
    tratamiento = Tratamiento.objects.all()
    medicina = Medicina.objects.all()
    tratamiento_medicina = TratamientoIndicacion.objects.all()
    context = {'cita': cita, 'tratamiento': tratamiento, 'medicina': medicina,
                'tratamiento_medicina': tratamiento_medicina}
    return render(request, "serina_views/ver_tratamiento.html",context)

def view_tratamiento(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    tratamiento = request.GET.get("tratamiento","")
    obj_tratamiento = Tratamiento.objects.get(pk = tratamiento)
    tratamiento_indicacion = TratamientoIndicacion.objects.all()
    cita = Cita.objects.all()
    medicina = Medicina.objects.all()
    dosis = Dosis.objects.all()
    categoria = Categoria.objects.all()
    tipo_medicamento = TipoMedicamento.objects.all()
    indicacion = Indicacion.objects.all()
    context = {'cita': cita, 'tratamiento': obj_tratamiento, 'medicina': medicina, 'tratamiento_indicacion': tratamiento_indicacion,
                'dosis': dosis, 'tipo_medicamento': tipo_medicamento,'categoria': categoria, 'indicacion': indicacion}
    return render(request, "serina_views/info_tratamiento.html", context)



def show_indicaciones(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    cita = request.GET.get("cita","")
    obj_cita = Cita.objects.get(pk = cita)
    obj_categoria = Categoria.objects.all()
    obj_medicina = Medicina.objects.all()
    context = {'cita' : obj_cita, 'categoria' : obj_categoria, 'medicina': obj_medicina}
    return render(request, "serina_views/form_indicaciones.html", context)

def add_indicaciones(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    medicina = request.POST['info_medicina']
    info = medicina.split("|$")
    nombre_medicina = info[0]
    dosis_medicina = info[1]
    concentracion_medicina = info[2]

    cita = request.POST['citas_form']
    fecha_inicio_ind = request.POST['fecha_inicio_ind']
    fecha_final_ind = request.POST['fecha_final_ind']
    fecha_recipe_tra = request.POST['fecha_recipe_tra']
    cantidad_dosis = request.POST['cantidad_dosis']
    dif_horas = request.POST['dif_horas']
    tra_continuo = request.POST.get('tra_continuo', False)

    if tra_continuo:
        tra_continuo = True

    id_cita = Cita.objects.get(pk = cita)
    obj_tratamiento = Tratamiento(continuo = tra_continuo, fecha_recipe = fecha_recipe_tra, id_cita = id_cita)
    obj_tratamiento.save()

    obj_medicina = Medicina.objects.filter(nombre = nombre_medicina, concentracion = concentracion_medicina,tipo_dosis =dosis_medicina)

    obj_indicacion = Indicacion(id_medicina = obj_medicina[0], fecha_inicio = fecha_inicio_ind, fecha_final = fecha_final_ind,
                                diferencia_horas = dif_horas, cantidad_dosis = cantidad_dosis)
    obj_indicacion.save()
    id_tratamiento = Tratamiento.objects.get(pk = obj_tratamiento.id)
    id_indicacion = Indicacion.objects.get(pk = obj_indicacion.id)
    tratamiento_indicacion = TratamientoIndicacion(id_tratamiento = id_tratamiento, id_indicacion = id_indicacion)
    tratamiento_indicacion.save()
    return redirect('show_tratamiento')

def add_tratamiento(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    return redirect('show_tratamiento')

def add_informacion(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    return render(request, "serina_views/form_informacion.html")

def show_login(request):
    return render(request, "serina_views/sign_in.html" )

def show_sign_up(request):
    return render(request, "serina_views/sign_up.html")

def add_sing_up(request):
    email = request.POST['cuenta']
    password = request.POST['password']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    ci = request.POST['cedula']
    nacimiento = request.POST['fecha_nacimiento']
    altura = request.POST['altura']

    user = User.objects.create_user(email, email, password)

    user.first_name = nombre
    user.last_name = apellido
    user.save()

    db_object = Usuario(email = user, nombre = nombre, apellido = apellido, ci = ci, fecha_nacimiento =nacimiento, altura = altura)
    db_object.save()
    return redirect('index')

def add_sing_in(request):
    username = request.POST['lemail']
    password = request.POST['lpassword']

    user = authenticate(request, username = username, password=password)

    if user is not None:
        login(request, user)
        request.session['user_email'] = user.email
        messages.success(request, 'Bienvenido')
        return redirect('show_categoria')
    else:
        messages.success(request, 'Datos Incorrectos')
        return redirect('show_login')

def logout_view(request):
    logout(request)

    try:
        del request.session['user_email']
    except KeyError:
        pass

    messages.success(request, 'Hasta Luego')
    return redirect('index')
