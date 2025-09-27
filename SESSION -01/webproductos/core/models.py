from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    imagen=models.ImageField(upload_to="productos/")




class Detalle(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    descripcion=models.TextField()
    stock=models.IntegerField
    color=models.CharField(max_length=50)

    def __str__(self):
       return  self.producto.nombre


    def __str__(self):
      return  f"{self.nombre}"