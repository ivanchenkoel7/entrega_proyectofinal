from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from blog.models import Article, Category, Avatar
from .forms import ContactoForm
from .forms import CategoryForm
from .forms import ArticleForm
from .forms import AvatarForm

# Create your views here.

def list(request):
    
    articles = Article.objects.all()
    
    return render(request,'articles/list.html',{
        'title': 'Articulos',
        'articles': articles
        
    })
    
def category(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)

    articles = Article.objects.filter(categories=category_id)
    
    return render (request,'categories\category.html',{
        'category': category,
        'articles': articles
    })
    
    

def article(request, article_id):
    
    article = get_object_or_404(Article, id=article_id)
    
    return render(request, 'articles/detail.html', {
        'article': article
    })
    
    
    
def contacto(request):
    data= {
        'form': ContactoForm()
        }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
        
    
    return render(request, 'contacto/contacto.html', data)


def categories(request):
    data = {
        'form': CategoryForm()
    }
    
    if request.method == 'POST':
        formulario = CategoryForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Categoria Creada"
            
        else:
            data["form"] = formulario
            
            
    return render(request, 'mainapp\category.html', data)


def articles(request):
    data = {
        'form': ArticleForm()
    }
    
    if request.method == 'POST':
        formulario = ArticleForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Descripcion Creada"
            
        else:
            data["form"] = formulario
            
            
    return render(request, 'mainapp/articulo.html', data)



def modificar_article(request, id):
    
    article = get_object_or_404(Article, id=id)
    
    data = {
        'form': ArticleForm(instance=article)
        
    }
    if request.method == 'POST':
        formulario = ArticleForm(data=request.POST, instance=article, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="list")
        
            
        else:
            data["form"] = formulario
            
    
    return render(request, 'mainapp\modificar.html', data)

def eliminar_articulo(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect(to="list")



    

