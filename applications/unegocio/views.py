from django.shortcuts import render
from django.urls import reverse_lazy #Sirve para redireccionar urls
from .models import Unegocio

from django.views.generic import(
        ListView
)

# Create your views here.

class ListAllUnegocios(ListView):
        model = Unegocio
        paginate_by=10
        template_name = "unegocio/list_all.html"
