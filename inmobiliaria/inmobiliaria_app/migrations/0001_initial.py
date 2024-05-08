# Generated by Django 5.0.4 on 2024-05-08 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.TextField()),
                ('m2_construidos', models.IntegerField()),
                ('m2_totales', models.IntegerField()),
                ('cant_estacionamientos', models.CharField(max_length=2)),
                ('cant_habitaciones', models.CharField(max_length=2)),
                ('cant_banios', models.CharField(max_length=2)),
                ('direccion', models.CharField(max_length=80)),
                ('comuna', models.CharField(max_length=30)),
                ('tipo_inmueble', models.CharField(choices=[('CASA', 'Casa'), ('DPTO', 'Departamento'), ('PARC', 'Parcela')], default='DPTO', max_length=12)),
                ('precio_mes_arriendo', models.IntegerField()),
                ('image', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('tipo_user', models.CharField(choices=[('ARRENDADOR', 'Arrendador'), ('ARRENDATARIO', 'Arrendatario')], default='ARRENDADOR', max_length=12)),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Inmueble',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('0', 'Aprobado'), ('1', 'Rechazado'), ('2', 'Pendiente')], default='2', max_length=12)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
                ('arrendatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='inmobiliaria_app.usuario')),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inmueble', to='inmobiliaria_app.inmueble')),
            ],
        ),
        migrations.AddField(
            model_name='inmueble',
            name='usuario',
            field=models.ManyToManyField(related_name='user_inmueble', through='inmobiliaria_app.Usuario_Inmueble', to='inmobiliaria_app.usuario'),
        ),
    ]