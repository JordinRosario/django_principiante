from django.shortcuts import render, redirect

from django.http import HttpResponse
""" Crea usuario y comprueba usucario  por medio de formulario"""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError
from .forms import TaskForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET': 
        return render(request, 'signup.html',{
        'form':UserCreationForm
    })
    else:
        print(request.POST)
        if request.POST['password1']==request.POST['password2']:
            #register user
            try:
                user =User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('task')
            except IntegrityError:
                return render(request, 'signup.html',{
                'form':UserCreationForm,
                'error':'Erro de integridad'
                })
            
        return render(request, 'signup.html',{
        'form':UserCreationForm,
        'error':'LAs claves no coinsiden'
        })

def task(request):
    return render(request, 'task.html')

def crear_task(request):
    if request.method == 'GET':
        return render(request, 'crear_task.html', {
        'form':TaskForm
    })
    else:
        print(request.POST)
        return render(request, 'crear_task.html', {
        'form':TaskForm
    })
    
    
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form':AuthenticationForm
        })
    else:
        user =authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:                   
            return render(request,'signin.html',{
                'form':AuthenticationForm,
                'error':'La clave o la contrasenia son incorrectas '
            })   
            
        else:
            login(request, user)
            return redirect('task')