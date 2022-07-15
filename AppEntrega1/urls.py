from django.urls import path, include
from AppEntrega1 import views
from AppEntrega1.views import *

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('administrador/', views.administrador, name= "Administrador"),
    path('empleado/', views.empleado, name= "Empleado"),
    path('cliente/', views.cliente, name= "Cliente"),
    path('adminFormulario/', views.administrador, name="AdminFormulario"),
    path('empleadoFormulario/', views.empleado, name="EmpleadoFormulario"),
    path('clienteFormulario/', views.cliente, name="ClienteFormulario"),
    path('busquedaNombre/', views.busquedaNombre, name="BusquedaNombre"),
    path('buscar/', views.buscar, name="Buscar"),

]