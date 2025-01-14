# Generated by Django 4.2.15 on 2025-01-10 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('orden', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Logro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('completado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('notas', models.TextField(blank=True)),
                ('bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprogreso.bloque')),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('puntos', models.IntegerField(default=0)),
                ('realizada', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('orden', models.IntegerField(default=0)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprogreso.tema')),
            ],
        ),
    ]
