from django.db import models

# Create your models here.

from applications.empresa.models import Empresa

class Unegocio(models.Model):
    ruc = models.CharField('Ruc', max_length=13,unique=True)
    nombre = models.CharField('Nombre', max_length=250)
    direccion = models.CharField('Direccion', max_length=250)
    contacto= models.CharField('Contacto', max_length=50)
    telefono = models.CharField('Telefono', max_length=50)
    correo = models.CharField('Correo Electronico', max_length=50)
    nombreContador= models.CharField('Nombre Contador', max_length=50,blank=True)
    rucContador= models.CharField('Ruc del Contador', max_length=50,blank=True)
    nombreRlegal= models.CharField('Nombre Representante Legal', max_length=50)
    rucRlegal= models.CharField('Ruc del Representante Legal', max_length=50)
    estado = models.BooleanField('Estado',default=True)
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    class Meta:
        verbose_name='Unegocio'
        ordering=['nombre']

    def __str__(self):
        return str(self.id) + '-' + self.ruc+ ' - ' + self.nombre