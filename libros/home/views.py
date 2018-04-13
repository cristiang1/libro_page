from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
#mostrar vista inicio y login
def Vista_index(request):
	usuario=""
	clave=""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['usuario']
			clave = formulario.cleaned_data['clave']
			user = authenticate(username = usuario, password = clave)
			if user is not None and user.is_active:
				login(request, user)
				return redirect("/administer/")
			else:
				msj = "usuario o clave incorrecto"
	formulario = login_form()

	#registro usuarios
	formulario = registro_user_form()
	if request.method=='POST':
		formulario = registro_user_form(request.POST)
		if formulario.is_valid():
			info_enviado=True
			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			contraseña = formulario.cleaned_data['password']
			confirmacion = formulario.cleaned_data['confipassword']
			u = User.objects.create_user(username=usuario, email=correo, password=contraseña )
			u = save()
			return redirect('/registro/')
		else:
			formulario = registro_user_form()
			
	return render(request, "index.html", locals())

#mostrar vista admin
def Vista_admin(request):
	libros_registrados = Libro.objects.all()
	return render(request, "admin.html", locals())

#metodo logout
def Vista_logout(request):
	logout(request)
	return redirect('inicio')

#mostrar vista busqueda_autor
def Vista_autor(request):
	info_enviado = False
	autor=""
	if request.method == "POST":
		formulario = autor_form(request.POST)
		if formulario.is_valid():
			info_enviado= True
			autor = formulario.cleaned_data['nombre_autor']
			lista = Autor.objects.filter(nombre__startswith=autor)
			codigo=0
			for x in lista:
				codigo=codigo+x.id
			lista_libros = Libro.objects.filter(id=codigo)
		return render(request,'autor.html', locals())
	else:
		formulario = autor_form()
	return render(request,'autor.html', locals())


#mostrar vista busqueda_libro
def Vista_libro(request):
	info_enviado = False
	libro=""
	if request.method == "POST":
		formularilibro = libro_form(request.POST)
		if formularilibro.is_valid():
			info_enviado= True
			libro = formularilibro.cleaned_data['titulo_libro']
			lista = Libro.objects.filter(titulo__startswith=libro)
		return render(request,'libro.html', locals())
	else:
		formularilibro = libro_form()
	return render(request,'libro.html', locals())

#agregar libro
def Vista_agregarl(request):
	if request.method=='POST':
		formulariol = agregar_libro_form(request.POST, request.FILES)
		if formulariol.is_valid():
			libro=formulariol.save(commit=False)
			libro.save()
			formulariol.save_m2m()
			return redirect('/administer/')
	else:
		formulariol= agregar_libro_form()

	return render(request, 'agregar_libro.html', locals())

#agregar editorial
def Vista_agregare(request):
	if request.method=='POST':
		formularioe = agregar_editorial_form(request.POST, request.FILES)
		if formularioe.is_valid():
			editoriae=formularioe.save(commit=False)
			editoriae.save()
			formularioe.save_m2m()
			return redirect('/index/')
	else:
		formularioe = agregar_editorial_form()

	return render(request, 'agregar_editorial.html',locals())


#agregar autor
def Vista_agregara(request):
	if request.method=='POST':
		formularioa = agregar_autor_form(request.POST, request.FILES)
		if formularioa.is_valid():
			autor=formularioa.save(commit=False)
			autor.save()
			formularioa.save_m2m()
			return redirect('/agregarautor/')
	else:
		formularioa = agregar_autor_form()

	return render(request, 'agregar_libro.html',locals())

#agregar genero
def Vista_agregarg(request):
	if request.method=='POST':
		formulariog = agregar_genero_form(request.POST, request.FILES)
		if formulariog.is_valid():
			genero=formulariog.save(commit=False)
			genero.save()
			formulariog.save_m2m()
			return redirect('/agregargenero/')
	else:
		formulariog= agregar_genero_form()

	return render(request, 'agregar_genero.html',locals())

#eliminar libro
def Vista_eliminarl(request):
	libro = ""
	infor_enviado = False
	codigo = 0
	if request.method == 'POST':
		formularioelim = eliminar_libro_form(request.POST)
		if formularioelim.is_valid():
			infor_enviado = True
			titulado = formularioelim.cleaned_data['eliminar_libro']
			libro = Libro.objects.filter(titulo = titulado)
			for i in libro:
				codigo = codigo + i.id
			eliminando = Libro.objects.get(id = codigo)
			eliminando.delete()
		return render(request, 'eliminarlibro.html', locals())
	else:
		formularioelim = eliminar_libro_form()

	return render(request, 'eliminarlibro.html', locals())

#eliminar genero
def Vista_eliminarg(request):
	genero = ""
	infor_enviado = False
	codigo = 0
	if request.method == 'POST':
		formulario = eliminar_genero_form(request.POST)
		if formulario.is_valid():
			infor_enviado = True
			nombreg = formulario.cleaned_data['eliminar_genero']
			genero = Genero.objects.filter(nombre_genero = nombreg)
			for i in genero:
				codigo = codigo + i.id
			eliminando = Genero.objects.get(id = codigo)
			eliminando.delete()
		return render(request, 'eliminargenero.html', locals())
	else:
		formulario = eliminar_genero_form()

	return render(request, 'eliminargenero.html', locals())

#eliminar autor
def Vista_eliminara(request):
	nombre = ""
	infor_enviado = False
	codigo = 0
	if request.method == 'POST':
		formulario = eliminar_autor_form(request.POST)
		if formulario.is_valid():
			infor_enviado = True
			nombrea = formulario.cleaned_data['eliminar_autor']
			nombre = Autor.objects.filter(nombre = nombrea)
			for i in nombre:
				codigo = codigo + i.id
			eliminando = Autor.objects.get(id = codigo)
			eliminando.delete()
		return render(request, 'eliminarautor.html', locals())
	else:
		formulario = eliminar_autor_form()

	return render(request, 'eliminarautor.html', locals())

#eliminar editorial
def Vista_eliminare(request):
	editora = ""
	infor_enviado = False
	codigo = 0
	if request.method == 'POST':
		formulario = eliminar_editorial_form(request.POST)
		if formulario.is_valid():
			infor_enviado = True
			nombree = formulario.cleaned_data['eliminar_editorial']
			editora = Editorial.objects.filter(nombre_editorial = nombree)
			for i in editora:
				codigo = codigo + i.id
			eliminando = Editorial.objects.get(id = codigo)
			eliminando.delete()
		return render(request, 'eliminareditorial.html', locals())
	else:
		formulario = eliminar_editorial_form()

	return render(request, 'eliminareditorial.html', locals())

def Vista_prueba(request):
	return render(request, 'pruebas.html', locals())

#registro usuarios
def Vista_registro(request):
	info_enviado=False
	return render(request, 'registro.html', locals())

