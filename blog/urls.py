from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.list, name="list"),
    path('categoria/<int:category_id>', views.category, name="category"),
    path('articulo/<int:article_id>', views.article, name="article"),
    path('mensaje/', views.contacto, name="mensaje"),
    path('category/', views.categories, name="Categoria"),
    path('arti/', views.articles, name="Articulo"),
    path('modificar_article/<id>/', views.modificar_article, name="modificar_article"),
    path('eliminar_article/<id>/', views.eliminar_articulo, name="eliminar_article"),
    
]
