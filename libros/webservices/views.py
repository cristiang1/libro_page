from django.shortcuts import render
from home.models import *
from .serializer import *
from rest_framework import viewsets
# Create your views here.
class libro_viewset(viewsets.ModelViewSet):
	queryset = Libro.objects.all()
	serializer_class = libro_serializer

class autor_viewset(viewsets.ModelViewSet):
	queryset = Autor.objects.all()
	serializer_class = autor_serializer

class genero_viewset(viewsets.ModelViewSet):
	queryset = Genero.objects.all()
	serializer_class = genero_serializer

class editorial_viewset(viewsets.ModelViewSet):
	queryset = Editorial.objects.all()
	serializer_class = editorial_serializer
