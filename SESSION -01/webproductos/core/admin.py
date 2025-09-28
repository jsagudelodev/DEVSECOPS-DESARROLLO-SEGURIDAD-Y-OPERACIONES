from django.contrib import admin
from .models import Producto,Detalle
# Register your models here.
admin.site.register([Producto,Detalle])
