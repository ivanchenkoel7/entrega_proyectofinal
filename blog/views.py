from django.shortcuts import render, get_object_or_404

from blog.models import Article, Category
from .forms import ContactoForm

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