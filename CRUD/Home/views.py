#Importaciones de Django
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Importaciones locales
from Home.forms import SignUpForm, LoginForm

# Create your views here.
def SignUp(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'SignUp.html', {'form':form})

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
        form = LoginForm()

    return render(request, 'login.html', {'form':form, 'error':'User or password incorrect'})

@login_required
def Logout(request):

    logout(request)

    return redirect('login')

@login_required
def Home(request):

    return HttpResponse('Hola Mundo: Home')