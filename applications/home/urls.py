from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.HomeView.as_view()),
   # path('new-empresa/', views.NewEmpresaView.as_view()),
   
]