# Generated by Django 4.2.15 on 2025-01-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oprogreso', '0004_logro_puntos_necesarios_alter_logro_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='logro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='logros/'),
        ),
    ]
