from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy #Sirve para redireccionar urls
from django.views.generic import (
        ListView,
        DetailView
)
from django.views.generic.edit import FormView

from .models import Empresa
from .forms import NewEmpresaForm

# Create your views here.
class ListAllEmpresas(ListView):
      #  model = Empresa
        paginate_by=10
        template_name = "empresa/list_all.html"

        def get_queryset(self):
            palabra_clave=self.request.GET.get("kword",'')
            lista=Empresa.objects.filter(
                  nombre__icontains=palabra_clave
            )
            return lista

class ListEmpresaByKword(ListView):
        template_name='empresa/by_kword.html'
        context_object_name='empresas'
        def get_queryset(self):
                palabra_clave=self.request.GET.get("kword",'')
                lista=Empresa.objects.filter(
                        nombre=palabra_clave
                )
                return lista
        
class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'empresa/detalle_empresa.html'
    
    def get_context_data(self, **kwargs):
        context = super(EmpresaDetailView, self).get_context_data(**kwargs)
        return context
    
class EmpresaDetailModalView(DetailView):
    model = Empresa
    form_class=NewEmpresaForm
    template_name = 'empresa/detalle_empresa.html'
    
    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(EmpresaDetailModalView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        empresa = Empresa.objects.get(id=self.id)
        return HttpResponse(render_to_string('empresa/list_all.html', {'empresa': empresa}))    
    



class NewEmpresaView(FormView):
        template_name='empresa/new_empresa.html'
        form_class=NewEmpresaForm
        success_url='/'

        def form_valid(self,form):                
                vruc = form.cleaned_data['vruc']
                vnombre = form.cleaned_data['vnombre']
                vdireccion = form.cleaned_data['vdireccion']
                vcontacto= form.cleaned_data['vcontacto']
                vtelefono = form.cleaned_data['vtelefono']
                vcorreo = form.cleaned_data['vcorreo']
                Empresa.objects.create(
                        ruc=vruc,
                        nombre=vnombre,
                        direccion=vdireccion,
                        contacto=vcontacto,
                        telefono=vtelefono,
                        correo=vcorreo,
                        estado=True
                )
                
                return super(NewEmpresaView,self).form_valid(form)
