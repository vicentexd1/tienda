from django import forms
from django.forms import ModelForm
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#CREAMOS TEMPLATES DE LOS FORMULARIOS

class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=6,max_length=25)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields = ['codigo','nombre','precio','stock','tipo','imagen',]
        
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario','contraseña','correo',]    

class RegistroUsuarioForm(UserCreationForm):
	class Meta:
            model = User
            fields = ['username','first_name','last_name','email','password1','password2',]               