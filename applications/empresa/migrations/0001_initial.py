# Generated by Django 4.2 on 2023-05-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=13, unique=True, verbose_name='Ruc')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=250, verbose_name='Direccion')),
                ('contacto', models.CharField(max_length=50, verbose_name='Contacto')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo Electronico')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Empresa',
                'ordering': ['nombre'],
            },
        ),
    ]
