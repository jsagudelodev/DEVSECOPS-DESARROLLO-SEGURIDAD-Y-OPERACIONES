from django.db import models


class Empleado(models.Model):
    nombre=models.CharField(max_length=100)
    puesto=models.CharField(max_length=50)
    salario=models.DecimalField(max_digits=10,decimal_places=2)
    fecha_contratacion=models.DateField()

    def __str__(self):
        return f"Empleado {self.nombre} - Su Cargo {self.puesto} -  Y percibe $ {self.salario}"


class FichaPersonal(models.Model):
    empleado=models.OneToOneField(Empleado,on_delete=models.CASCADE)
    dni=models.CharField(max_length=15,unique=True)
    direccion=models.CharField(max_length=200)
    telefono=models.CharField(max_length=20)

    def __str__(self):
        return f"Ficha de {self.empleado.nombre}"
    

class Proyecto(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()
    empleados=models.ManyToManyField(Empleado,related_name='proyectos')

    def __str__(self):
        return self.nombre


# Create your models here.
