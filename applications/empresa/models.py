from django.db import models

# Create your models here.
class Empresa(models.Model):
    ruc = models.CharField('Ruc', max_length=13,unique=True)
    nombre = models.CharField('Nombre', max_length=250)
    direccion = models.CharField('Direccion', max_length=250)
    contacto= models.CharField('Contacto', max_length=50)
    telefono = models.CharField('Telefono', max_length=50)
    correo = models.CharField('Correo Electronico', max_length=50)
    estado = models.BooleanField('Estado',default=True)
    
    class Meta:
        verbose_name='Empresa'
        ordering=['nombre']

    def __str__(self):
        return str(self.id) + '-' + self.ruc+ ' - ' + self.nombre