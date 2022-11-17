from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion' )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    title= models.CharField(max_length=50, verbose_name="Titulo")
    content= RichTextField(verbose_name="Contenido")
    image= models.ImageField(default='null', verbose_name='Imagen', upload_to="articles" )
    public= models.BooleanField(verbose_name='Publicado?')
    user= models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    categories= models.ManyToManyField(Category, verbose_name='Categorias', blank=True)
    created_at= models.DateTimeField(auto_now_add=True,verbose_name="Creado el")
    udapte_at= models.DateTimeField(auto_now=True,verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        
    def __str__(self):
        return self.title 
    
    