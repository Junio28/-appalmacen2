# Generated by Django 3.0.3 on 2020-03-27 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('rut', models.CharField(max_length=20, verbose_name='Cedula')),
                ('address', models.CharField(max_length=50, verbose_name='Direccion')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
