import requests
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

#SECCION AGREGAR
@permission_required('app.add_producto')
def agregar(request):
    datos= {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')

    return render(request, 'app/agregar.html', datos)

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/Login.html') 

def historial(request):
    carrito = Items_Carrito.objects.all()
    datos = { 'listaCarrito' : carrito }

    return render(request, 'app/historial.html', datos)     



#SECCION LISTAR

@login_required     
def productos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaproductos' : productosAll

    }
    if request.method == 'POST':
        carrito = Items_Carrito()
        carrito.codigo_carrito = request.POST.get('codigo_carrito')
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    return render(request, 'app/productos.html' , datos)    

def productosapi(request):
    productosAll = Producto.objects.all()
    response = requests.get('https://digimon-api.vercel.app/api/digimon').json()
    datos = {
        'listaJson' : response

    }
    if request.method == 'POST':
        carrito = Items_Carrito()
        carrito.codigo_carrito = request.POST.get('codigo_carrito')
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    return render(request, 'app/productosapi.html' , datos) 


def registrarse(request):
    return render(request, 'app/Registrarse.html')

@login_required    
def seguimiento(request):
    return render(request, 'app/Seguimiento.html')


@login_required
def carrito(request):
    carrito = Items_Carrito.objects.all()
    datos = { 'listaCarrito' : carrito }

    return render(request, 'app/Carrito.html', datos)


@login_required
def usuariosub(request):
    return render(request, 'app/usuario-sub.html')


@login_required
def usuariodesub(request):
    return render(request, 'app/usuario-desub.html')


@permission_required('app.view_producto')
def listar(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaproductos' : productosAll
    }

    return render(request, 'app/listar.html' , datos) 

@permission_required('app.change_producto')                                             
def modificar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto Modificado correctamente!')
            datos['form'] = formulario

    return render(request, 'app/modificar.html  ', datos)


@permission_required('app.delete_producto')
def eliminar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar") 

def eliminar2(request, codigo_carrito):
    carrito = Items_Carrito.objects.get(codigo_carrito=codigo_carrito)
    carrito.delete()

    return redirect(to="Carrito") 

def agregarusuario(request):
    datos= {
        'form' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario guardado correctamente!')

    return render(request, 'app/agregarusuario.html', datos)


def registro(request):
    datos = { 'form' : RegistroUsuarioForm() }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario registrado correctamente!')
    return render(request, 'registration/registro.html', datos)


def eliminarcarrito(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar") 

def successful(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()

    return render(request, 'app/successful.html')