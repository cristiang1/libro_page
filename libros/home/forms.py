from django import forms
from .models import *
from django.contrib.auth.models import User

#login
class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'USUARIO'}))
	clave = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'placeholder': 'CONTRASEÑA'}))

#busqueda por autor
class autor_form(forms.Form):
	nombre_autor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre autor'}))

#busqueda por libro
class libro_form(forms.Form):
	titulo_libro = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Titulo del libro'}))

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

#registrar usuario
class registro_user_form(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'USUARIO'}))
	email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder': 'EMAIL'}))
	password = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'placeholder': 'CONTRASEÑA'}))
	confipassword = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'placeholder': 'CONFIRMAR CONTRASEÑA'}))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username

		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try: 
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')

	def clean_password_two(self):
		password =self.cleaned_data['password']
		confipassword = self.cleaned_data['confipassword']
		if password == confipassword:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')