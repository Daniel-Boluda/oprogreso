from django.contrib import admin
from .models import Bloque, Tema, Actividad, Logro

class BloqueAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')  # Display these fields in the list view
    search_fields = ('titulo',)  # Enable search functionality

class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'bloque', 'orden')
    search_fields = ('titulo',)

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'realizada' , 'fecha'  , 'puntos')
    list_filter = ('realizada',)

class LogroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puntos_necesarios', 'completado')
    search_fields = ('nombre',)

# Register your models here.
admin.site.register(Bloque, BloqueAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Logro, LogroAdmin)
