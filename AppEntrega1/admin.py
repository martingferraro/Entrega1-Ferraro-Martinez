from django.contrib import admin

from AppEntrega1.views import administrador
from .models import *


# Register your models here.


admin.site.register(Administrador)
admin.site.register(Empleado)
admin.site.register(Cliente)