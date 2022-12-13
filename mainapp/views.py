import os
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from blog.models import Article, Avatar, Category
from blog.forms import AvatarForm
from mainapp.forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio',
    
    })
    
    
def avatar(request):
    imagenes = Avatar.objects.filter(user=request.user.id)
    return render(request, 'mainapp/index.html', {
    'url': imagenes[0].imagen.url})


def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Acerca de nosotros'
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

    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')

        else:
            messages.warning(request, 'No te has identificado correctamente :')

    return render(request, 'users/login.html', {
        'title': 'Identificate'

    })
    

    


def logout_user(request):
    logout(request)
    return redirect('login')



