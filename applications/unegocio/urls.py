from django.contrib import admin
from django.urls import path
from . import views

app_name='unegocio_app'

urlpatterns = [
   path('listar-unegocios/', views.ListAllUnegocios.as_view(),name='unegocio.all'),
   
]