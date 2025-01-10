from django.contrib import admin
from .models import Bloque, Tema, Actividad, Logro

# Register your models here.
admin.site.register(Bloque)
admin.site.register(Tema)
admin.site.register(Actividad)
admin.site.register(Logro)