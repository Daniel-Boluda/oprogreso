# Generated by Django 4.2.15 on 2025-01-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oprogreso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tema',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
    ]
