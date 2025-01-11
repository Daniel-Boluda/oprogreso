from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Logro, Bloque, Tema, Actividad

def homepage(request):
    bloques = Bloque.objects.all()
    actividades = Actividad.objects.filter(realizada=True)
    puntos_totales = sum(a.puntos for a in actividades)
    
    logros = Logro.objects.order_by('puntos_necesarios')
    alcanzados = logros.filter(puntos_necesarios__lte=puntos_totales)
    siguientes = logros.filter(puntos_necesarios__gt=puntos_totales)
    
    if alcanzados.count() >= 3:
        logros_a_mostrar = list(alcanzados[-3:]) + list(siguientes[:3])
    else:
        logros_a_mostrar = list(siguientes[:6])
    
    puntos_totales_requeridos = logros.last().puntos_necesarios if logros.exists() else 0
    porcentaje = (puntos_totales / puntos_totales_requeridos) * 100 if puntos_totales_requeridos > 0 else 0

    return render(request, 'home.html', {
        'bloques': bloques,
        'logros': logros_a_mostrar,
        'puntos_totales': puntos_totales,
        'puntos_totales_requeridos': puntos_totales_requeridos,
        'porcentaje': porcentaje,
    })

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def marcar_actividad(request, actividad_id):
    if request.method == 'POST':
        try:
            actividad = Actividad.objects.get(id=actividad_id)
            actividad.realizada = True
            actividad.save()
            return JsonResponse({'status': 'success'})
        except Actividad.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Actividad no encontrada'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def bloques_list(request):
    bloques = Bloque.objects.all().order_by('orden')
    return render(request, 'bloques_list.html', {'bloques': bloques})

# Vista para obtener datos de los logros dinámicamente
def obtener_logros(request):
    # Supongamos que estos datos vienen de la base de datos
    logros = [
        {"puntos": 100, "estado": "reached", "recompensa": None},
        {"puntos": 250, "estado": "reached", "recompensa": None},
        {"puntos": 500, "estado": "next", "recompensa": 100},
        {"puntos": 750, "estado": "locked", "recompensa": None},
        {"puntos": 1000, "estado": "locked", "recompensa": None},
    ]
    total_puntos = 500  # Puntos del usuario, ajusta según lógica
    return JsonResponse({"logros": logros, "total_puntos": total_puntos})
