#Importaciones de Django
from turtle import title
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Home.models import Cursos

#Importaciones locales
from Home.forms import SignUpForm, LoginForm, AgregarCursosForm, ModificarForm

# Create your views here.
def Login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form':form, 'error':'User or password incorrect'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form })

def SignUp(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'SignUp.html', {'form':form})

@login_required
def Logout(request):

    logout(request)

    return redirect('login')

@login_required
def Home(request):

    asignaturas = Cursos.objects.all()

    return render(request, 'home.html', {'asignaturas':asignaturas})

@login_required
def Agregar(request):

    if request.method == 'POST':
        form = AgregarCursosForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AgregarCursosForm()

    return render(request, 'agregar.html', {'form':form})

@login_required
def Modificar(request, id_asignatura):

    asignatura = Cursos.objects.get(id = id_asignatura)

    if request.method == 'POST':
        form = AgregarCursosForm(request.POST, instance=asignatura)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AgregarCursosForm(initial={'creditos':asignatura.creditos, 'nombre_asignatura':asignatura.nombre_asignatura, 'costo':asignatura.costo})

    return render(request, 'modificar.html', {'form':form, 'asignatura':asignatura})