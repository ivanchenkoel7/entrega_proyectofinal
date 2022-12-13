from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto
from .models import Category
from .models import Article
from .models import Avatar


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'
        
        
class CategoryForm(forms.ModelForm):
    
    
    class Meta:
        model = Category
        fields = '__all__'
        
        
        
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
class AvatarForm(forms.ModelForm):
    
    
    class Meta:
        model = Avatar
        fields = '__all__'