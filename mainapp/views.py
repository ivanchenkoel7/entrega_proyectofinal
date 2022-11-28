from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title' : 'Inicio'
    })
    
    
    
def about(request):
    return render( request, 'mainapp/about.html', {
        'title' : 'Acerca de nosotros'
    })
    
    
def register_page(request):
    if request.user.is_authenticated:
        return redirect('inicio')
        
    else:
        register_form = RegisterForm()
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Has sido registrado de forma correcta')
            
            return redirect('inicio')
            
    
    return render( request, 'users/register.html', {
        'title' : 'Registro',
        'register_form' : register_form
    })
    
    
def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request,user)
            return redirect('inicio')
        
        else:
            messages.warning(request, 'No te has identificado correctamente :' )
        
    
    
    
    return render(request, 'users/login.html', {
        'title': 'Identificate'
        
    })
    
def logout_user(request):
    logout(request)
    return redirect('login')

