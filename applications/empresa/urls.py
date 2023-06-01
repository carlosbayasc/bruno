from django.contrib import admin
from django.urls import path
from . import views

app_name="empresa_app"

urlpatterns = [
   path('listar-empresas/', views.ListAllEmpresas.as_view(),name='empresa.all'),
   path('detalle-empresa/<pk>/', views.EmpresaDetailModalView.as_view(),name='empresa.detalle'),
   path('new-empresa/', views.NewEmpresaView.as_view(),name='empresa.new'),
   
]