from django.db import models

# Create your models here.

class Administrador(models.Model):

    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    def __str__(self):
        return self.nombre+" "+str(self.apellido)

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return self.nombre+" "+str(self.apellido)+"                           "+str(self.email)


class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.nombre+" "+str(self.apellido)+"                           "+str(self.email)