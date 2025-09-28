
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),# Se agrega url nuevas en  las vistas
]
