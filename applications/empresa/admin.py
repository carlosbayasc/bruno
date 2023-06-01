from django.contrib import admin

from .models import Empresa
# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display=(
        'ruc', 
        'nombre',  
        'correo',
        'estado',
        'id'
    )
    search_fields=('nombre',)
    list_filter=('estado',)
    #filter_horizontal=('usuarios',)
    
admin.site.register(Empresa,EmpresaAdmin)
