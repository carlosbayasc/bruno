from django.contrib import admin

from .models import Unegocio
# Register your models here.

class UnegocioAdmin(admin.ModelAdmin):
    list_display=(
        'empresa',
        'ruc', 
        'nombre',  
        'correo',
        'estado',
        'id'
    )
    search_fields=('nombre',)
    list_filter=('estado',)
    #filter_horizontal=('usuarios',)
    
admin.site.register(Unegocio,UnegocioAdmin)
