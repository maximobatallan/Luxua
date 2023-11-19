from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import DatosForm, ProductForm, CategoriaForm
from .models import  Producto, Categoria
from django.contrib.auth.decorators import login_required
# Create your views here.
from .carrito import Carrito



def home(request):
    productos = Producto.objects.filter(important=True)
    cat = Categoria.objects.all()

    # Creamos un diccionario para agrupar los productos por categoría
    categorias_productos = {}
    
    for producto in productos:
        id = producto.id
        categoria = producto.cat
     

        if categoria in categorias_productos:
            categorias_productos[categoria].append(id)
        else:
            categorias_productos[categoria] = [id]
    
  
   
    return render(request, "home.html", {'categorias_productos': categorias_productos, 'productos': productos, 'cat': cat} )




def signup(request):
    if request.method == 'GET':
        
        return render(request, 'signup.html',{'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('gallery')
            except IntegrityError:
                return render(request, 'signup.html',{'form': UserCreationForm, "error":'Usuario ya existe'})
            
            
        return render(request, 'signup.html',{'form': UserCreationForm, "error":'La contraseña de verificación no coincide.'})


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        if 'submit_get' in request.POST:
            return render(request, 'signin.html', {"form": AuthenticationForm})
        else:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render (request, 'signin.html',{'form': AuthenticationForm, "error":'Usuario o pass incorrecto'})
            else:
                

                login(request, user)
                return redirect('gallery')


        
        
    
@login_required
def producto(request):
    
    if request.method == 'GET':
        return render(request, 'datos.html', {'form': DatosForm, 'form1': ProductForm, 'form2': CategoriaForm})
    else:
        print('post')
        try:
            form1 = ProductForm(request.POST, request.FILES)
            new_producto = form1.save(commit=False)
            new_producto.user = request.user
            new_producto.save()
            
            return redirect('datos')
        except ValueError:
            return render(request, 'datos.html', {'form1': ProductForm, 'error':'Por favor ingresos los datos validos'})
 



@login_required
def delete (request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)  
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
    
@login_required
def datos(request):
    if request.method == 'GET':
       
        return render(request, 'datos.html', {'form': DatosForm, 'form1': ProductForm, 'form2': CategoriaForm})
    else:
        try:
            form = DatosForm(request.POST)
            new_datos = form.save(commit=False)
            new_datos.user = request.user
            new_datos.save() 
            return redirect('datos')
        except ValueError:
            return render(request, 'datos.html', {'form': DatosForm, 'error':'Por favor ingresos los datos validos'})

@login_required
def categoria(request):
    if request.method == 'GET':
        return render(request, 'datos.html', {'form': DatosForm, 'form2': CategoriaForm})
    else:
        try:
            form = CategoriaForm(request.POST)
            new_datos = form.save(commit=False)
            new_datos.user = request.user
            new_datos.save() 
            return redirect('datos')
        except ValueError:
            print ('aca')
            return render(request, 'datos.html', {'form': DatosForm, 'error':'Por favor ingresos los datos validos'})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("cart")
 

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.eliminar(producto)
   
    return redirect("cart")
    
    
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")


def limpiar_carrito_item(request,producto_id):
    
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.limpiaritem(producto)
    return redirect("cart")


def galeriaprueba(request):
    productos = Producto.objects.all()
   
    return render(request, "gallery.html", {'productos': productos})


def detalleproducto(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
   
    return render(request, "productdetails.html", {'productos': producto})
    
    
    




def catproducto(request, catproducto):
    productos = Producto.objects.filter(cat = catproducto)
    cat = Categoria.objects.all()
    return render(request, "categoriaproducto.html", {'productos': productos, 'cat': cat})