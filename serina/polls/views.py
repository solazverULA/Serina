from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormCategoria, FormUsuario
from .models import Categoria
from .models import Cita
from .models import Usuario
from .models import Tratamiento
from .models import TipoMedicamento
from .models import Dosis
from .models import Medicina
from .models import Indicacion
from .models import TratamientoMedicina

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'serina_views/index.html')

def view_categoria(request):
    return render(request, 'serina_views/ver_categ.html')

def add_categoria(request):

    nombre = request.POST['categoria']
    categoria = nombre.lower()
    obj = Categoria.objects.all()
    for i in obj:
        nombres = i.nombre.lower()
        if(categoria == nombres):
            return HttpResponse("ERROR. ESTA AGREGANDO UNA CATEGORIA QUE YA EXISTE")
    context = {'categoria': categoria}
    db_o = Categoria(nombre=categoria)
    db_o.save()
    return redirect('show_categoria')

def add_medicina(request):
    medicina = request.POST['medicina']
    tipo_medicamento = request.POST['tipo_medicamento']
    tipo_dosis = request.POST['tipo_dosis']
    nombre = medicina.lower()
    obj = Medicina.objects.all()
    for i in obj:
        medicinas = i.nombre.lower()
        if(nombre == medicinas):
            return("ERROR. ESTA AGREGANDO UNA MEDICINA QUE YA EXISTE")
    context = {'medicina': nombre}
    obj_dosis = Dosis(tipo = tipo_dosis)
    obj_dosis.save()
    obj_tipo_medicamento = TipoMedicamento(nombre = tipo_medicamento)
    obj_tipo_medicamento.save()
    pk_dosis = Dosis(pk = tipo_dosis)
    pk_medicamento = TipoMedicamento(pk = tipo_medicamento)
    obj_medicina = Medicina(nombre = medicina, tipo_medicamento = pk_medicamento, tipo_dosis = pk_dosis)
    obj_medicina.save()
    return redirect('show_categoria')

def add_cita(request):
    categoria = request.POST['categ']
    fecha = request.POST['fechaa']
    nota = request.POST['notaa']
    email = Usuario.objects.get(pk ='kathesm903@gmail.com')
    id_categ = Categoria.objects.get(pk = categoria)
    cita = Cita(fecha = fecha, nota = nota, email_usuario = email, id_categoria = id_categ)
    cita.save()
    return redirect('show_categoria')

def show_categoria(request):
    categoria = Categoria.objects.all()
    cita = Cita.objects.all
    tratamiento = Tratamiento.objects.all()
    context = {'categoria': categoria, 'cita': cita, 'tratamiento': tratamiento}
    return render(request, 'serina_views/ver_categ.html', context)

def delete_categoria(request):
    categoria = request.GET.get("categoria","")
    cita = Cita.objects.all()
    eliminar = Categoria.objects.get(pk = categoria)
    eliminar.delete()
    return redirect('show_categoria')

def show_tratamiento(request):
    cita = Cita.objects.all()
    tratamiento = Tratamiento.objects.all()
    context = {'cita': cita, 'tratamiento': tratamiento}
    return render(request, "serina_views/ver_tratamiento.html",context)

def view_tratamiento(request):
    tratamiento = request.GET.get("tratamiento","")
    obj_tratamiento = Tratamiento.objects.get(pk = tratamiento)
    tratamiento_medicina = TratamientoMedicina.objects.all()
    categoria = Categoria.objects.all()
    cita = Cita.objects.all()
    tratamiento = Tratamiento.objects.all()
    medicina = Medicina.objects.all()
    dosis = Dosis.objects.all()
    tipo_medicamento = TipoMedicamento.objects.all()
    indicacion = Indicacion.objects.all()
    context = {'cita': cita, 'tratamiento': obj_tratamiento, 'medicina': medicina,
                'dosis': dosis, 'tipo_medicamento': tipo_medicamento, 'indicacion': indicacion,
                'tratamiento_medicina': tratamiento_medicina, 'categoria': categoria}
    return render(request, "serina_views/info_tratamiento.html", context)



def show_indicaciones(request):
    cita = request.GET.get("cita","")
    obj_cita = Cita.objects.get(pk = cita)
    obj_categoria = Categoria.objects.all()
    obj_medicina = Medicina.objects.all()
    context = {'cita' : obj_cita, 'categoria' : obj_categoria, 'medicina': obj_medicina}
    return render(request, "serina_views/form_indicaciones.html", context)

def add_indicaciones(request):
    nombre_medicina = request.POST['nombre_medicina']
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

    obj_medicina = Medicina.objects.get(pk = nombre_medicina)
    obj_indicacion = Indicacion(nombre_medicina = obj_medicina, fecha_inicio = fecha_inicio_ind, fecha_final = fecha_final_ind,
                                diferencia_horas = dif_horas, cantidad_dosis = cantidad_dosis)
    obj_indicacion.save()
    id_tratamiento = Tratamiento.objects.get(pk = obj_tratamiento.id)
    tratamiento_medicina = TratamientoMedicina(id_tratamiento = id_tratamiento, nombre_medicina = obj_medicina)
    tratamiento_medicina.save()
    return redirect('show_tratamiento')

def add_tratamiento(request):
    return redirect('show_tratamiento')

def add_informacion(request):
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
    db_object = Usuario(email = email, contrasena = password, nombre = nombre, apellido = apellido, ci = ci, fecha_nacimiento =nacimiento, altura = altura)
    db_object.save()
    return render(request, "serina_views/index.html")

def add_sing_in(request):
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
