from django.contrib import admin
from .models import Page

# Register your models here.

admin.site.register(Page)

#configuracion del panel de control

title = "Panel de Gestion"
subtitle = "Proyecto Final"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle