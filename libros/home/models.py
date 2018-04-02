from django.db import models

# Create your models here.
class Autor(models.Model):
	nombre = models.CharField(max_length = 100)
	edad = models.IntegerField()
	foto = models.ImageField(upload_to = 'img_autor', null=True, blank=True)

	def __str__(self):
		return self.nombre

class Libro(models.Model):
	titulo = models.CharField(max_length = 100)
	prologo = models.TextField(max_length = 500)
	ciudad_publicacion = models.CharField(max_length = 100)
	fecha_publicacion = models.DateField()
	num_paginas = models.IntegerField()
	traduccion = models.BooleanField()
	titulo_traduccion = models.CharField(max_length = 100)
	codigo_isbn = models.CharField(max_length = 10)
	portada = models.ImageField(upload_to = 'img_libro', null=True, blank=True)
	autor = models.ManyToManyField(Autor, null = True, blank = True)
	
	def __str__(self):
		return self.titulo

class Editorial(models.Model):
	nombre_editorial = models.CharField(max_length = 100)
	ciudad_editorial = models.CharField(max_length = 100)
	logo = models.ImageField(upload_to = 'img_editorial', null=True, blank=True)
	libro = models.ManyToManyField(Libro, null = True, blank = True)
	
	def __str__(self):
		return self.nombre_editorial

class Genero(models.Model):
	nombre_genero = models.CharField(max_length = 100)
	libro = models.ManyToManyField(Libro, null = True, blank = True)

	def __str__(self):
		return self.nombre_genero

