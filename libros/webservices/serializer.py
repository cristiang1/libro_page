from rest_framework import serializers
from home.models import *

class libro_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Libro
		fields = ('url', 'titulo', 'prologo', 'ciudad_publicacion', 'fecha_publicacion', 'num_paginas', 'traduccion', 'titulo_traduccion', 'codigo_isbn', 'portada', 'autor')

class autor_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Autor
		fields = ('url', 'nombre', 'edad', 'foto') 

class genero_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Genero
		fields = ('url', 'nombre_genero')

class editorial_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Editorial
		fields = ('url', 'nombre_editorial', 'ciudad_editorial', 'logo')		 				 