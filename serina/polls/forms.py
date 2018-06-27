from django import forms

from .models import Categoria, Usuario

class FormCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ["nombre"]

class FormUsuario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ["email", "nombre", "apellido", "ci", "fecha_nacimiento", "altura"]
