from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    color = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre