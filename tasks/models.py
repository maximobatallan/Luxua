from django.db import models


# Create your models here.

    
class Categoria(models.Model):
    cat = models.CharField(max_length=64)
    imagen = models.ImageField(upload_to='products/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.cat}"

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    important = models.BooleanField(default=False)
    cat = models.CharField(max_length=64)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='products/', null=True, blank=True)
    imagen1 = models.ImageField(upload_to='products/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='products/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre}: {self.precio}"
    
    
class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    nacionalidad = models.CharField(max_length=64)
    ciudad = models.CharField(max_length=64)
    telefono = models.IntegerField()
    nombreempresa = models.CharField(max_length=100)
    cbu = models.IntegerField()
    titular = models.CharField(max_length=64)
    descripcionempresa = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}: {self.nombreempresa}"
    
