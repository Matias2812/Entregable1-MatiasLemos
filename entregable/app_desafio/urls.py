from django.urls import path
from app_desafio.views import *

urlpatterns=[

    path('', inicio),
    path('datos_autos', auto_datos, name='autos'),
    path('datos_perros', perros_datos, name='perros'),
    path('datos_oficinas', oficinas_datos, name='oficinas'),
    path('buscar_autos', busqueda_autos, name='busqueda1'),
    path('buscar_perros', busqueda_perros, name='busqueda2'),
    path('buscar_oficinas', busqueda_oficinas, name='busqueda3'),
    path('busqueda_autos', auto_busqueda),
    path('busqueda_perros', perros_busqueda),
    path('busqueda_oficinas', oficinas_busqueda),
    


]