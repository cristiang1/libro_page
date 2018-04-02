from django import forms
from .models import *

#login
class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'USUARIO'}))
	clave = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'placeholder': 'CONTRASEÑA'}))

#busqueda por autor
class autor_form(forms.Form):
	nombre_autor = forms.CharField(widget=forms.TextInput())

#busqueda por libro
class libro_form(forms.Form):
	titulo_libro = forms.CharField(widget=forms.TextInput())

#agregar libro
class agregar_libro_form(forms.ModelForm):
	class Meta:
		model = Libro
		fields = '__all__'

#agregar genero
class agregar_genero_form(forms.ModelForm):
	class Meta:
		model = Genero
		fields = '__all__'

#agregar editorial
class agregar_editorial_form(forms.ModelForm):
	class Meta:
		model = Editorial
		fields = '__all__'

#agregar autor
class agregar_autor_form(forms.ModelForm):
	class Meta:
		model = Autor
		fields = '__all__'

#eliminar libro
class eliminar_libro_form(forms.Form):
	eliminar_libro = forms.CharField(widget = forms.TextInput())

#eliminar genero
class eliminar_genero_form(forms.Form):
	eliminar_genero = forms.CharField(widget=forms.TextInput())

#eliminar editorial
class eliminar_editorial_form(forms.Form):
	eliminar_editorial = forms.CharField(widget=forms.TextInput())

#eliminar autor
class eliminar_autor_form(forms.Form):
	eliminar_autor = forms.CharField(widget=forms.TextInput())