from django.contrib import admin
from .models import Acervo

# Register your models here.

@admin.register(Acervo)
class AcervoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipoObra', 'tituloObra', 'begin_date', 'description' , 'user']