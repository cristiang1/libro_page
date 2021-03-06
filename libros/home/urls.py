from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   	path('autor/', Vista_autor, name="autor"),
   	path('libro/', Vista_libro, name="libros"),
   	path('', Vista_index, name="inicio"),
   	path('administer/', Vista_admin, name="admin"),
   	path('agregarlibro/', Vista_agregarl, name="agregarl"),
   	path('eliminarlibro/', Vista_eliminarl, name="eliminarl"),
   	path('eliminargenero/', Vista_eliminarg, name="eliminarg"),
      path('eliminarautor/', Vista_eliminara, name="eliminara"),
      path('eliminareditorial/', Vista_eliminare, name="eliminare"),
      path('prueba/', Vista_prueba, name="pruebas"),
      path('logout/', Vista_logout, name="cierre"),
      path('registro/', Vista_registro, name="registro"),
      
]