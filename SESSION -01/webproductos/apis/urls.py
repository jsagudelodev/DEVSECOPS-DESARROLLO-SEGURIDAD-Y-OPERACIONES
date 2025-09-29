from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet,ArticulosListCreateAPIView


"""
#1  Una forma  de exponer las url
router=DefaultRouter()
router.register('articulos',ArticuloViewSet)## Url de entra a la api

urlpatterns = [
    path('',include(router.urls))    
]
"""

urlpatterns = [
   
    path('articuloslist/',ArticulosListCreateAPIView.as_view())
]



