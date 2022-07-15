from django.http import HttpResponse
from django.shortcuts import render
from AppEntrega1.forms import *
from AppEntrega1 import *
from AppEntrega1.models import Administrador, Cliente, Empleado
# Create your views here.

def inicio(request):
    return render(request, "AppEntrega1/inicio.html")

def administrador(request):
    return render(request, "AppEntrega1/administrador.html")

def empleado(request):
    return render(request, "AppEntrega1/empleado.html")

def cliente(request):
    return render(request, "AppEntrega1/cliente.html")


def administrador(request):
    if (request.method == "POST"):
        form=AdminFormulario(request.POST)
        print(form)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            administrador= Administrador(nombre=nombre, apellido=apellido, email=email)
            administrador.save()
            return render(request, "AppEntrega1/inicio.html")

    else:
        form= AdminFormulario ()
    return render (request,"AppEntrega1/formulario.html", {"form":form})

def empleado(request):
    if (request.method == "POST"):
        form=EmpleadoFormulario(request.POST)
        print(form)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            empleado= Empleado(nombre=nombre, apellido=apellido, email=email)
            empleado.save()
            return render(request, "AppEntrega1/inicio.html")

    else:
        form= EmpleadoFormulario ()
    return render (request,"AppEntrega1/empleadoFormulario.html", {"form":form})

def cliente(request):
    if (request.method == "POST"):
        form=ClienteFormulario(request.POST)
        print(form)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            cliente= Cliente(nombre=nombre, apellido=apellido, email=email)
            cliente.save()
            return render(request, "AppEntrega1/inicio.html")

    else:
        form= ClienteFormulario ()
    return render (request,"AppEntrega1/clienteFormulario.html", {"form":form})


def busquedaNombre(request):
    return render(request, "AppEntrega1/busquedaNombre.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        cliente= Cliente.objects.filter(nombre=nombre)
        return render(request, "AppEntrega1/resultadosBusqueda.html", {"cliente":cliente})
    else:
         return render(request, "AppEntrega1/busquedaNombre.html", {"error": "No se encontro el nombre"})
    