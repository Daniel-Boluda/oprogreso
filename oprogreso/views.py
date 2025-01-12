from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from .models import Logro, Bloque, Tema, Actividad

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def marcar_actividad(request, actividad_id):
    if request.method == 'POST':
        try:
            actividad = Actividad.objects.get(id=actividad_id)
            actividad.realizada = True
            actividad.save()
            
            actividades = Actividad.objects.filter(realizada=True)
            total_puntos = actividades.aggregate(Sum('puntos'))['puntos__sum'] or 0
            
            logros = Logro.objects.order_by('puntos_necesarios')
            logros_data = []
            
            for logro in logros:
                if logro.puntos_necesarios <= total_puntos:
                    estado = 'reached'
                elif logro == logros.filter(puntos_necesarios__gt=total_puntos).first():
                    estado = 'next'
                else:
                    estado = 'locked'
                
                logros_data.append({
                    'nombre': logro.nombre,
                    'puntos': logro.puntos_necesarios,
                    'estado': estado,
                    'descripcion': logro.descripcion,
                })
            
            return JsonResponse({
                'status': 'success',
                'logros': logros_data,
                'total_puntos': total_puntos
            })
        except Actividad.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Actividad no encontrada'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def bloques_list(request):
    bloques = Bloque.objects.all().order_by('orden')
    actividades = Actividad.objects.filter(realizada=True)
    puntos_totales = actividades.aggregate(Sum('puntos'))['puntos__sum'] or 0
    
    logros = Logro.objects.order_by('puntos_necesarios')
    alcanzados = logros.filter(puntos_necesarios__lte=puntos_totales)
    siguientes = logros.filter(puntos_necesarios__gt=puntos_totales)
    
    if alcanzados.count() >= 3:
        logros_a_mostrar = list(alcanzados.order_by('-puntos_necesarios')[:3]) + list(siguientes[:3])
    else:
        logros_a_mostrar = list(alcanzados) + list(siguientes[:6-alcanzados.count()])
    
    puntos_totales_requeridos = logros.last().puntos_necesarios if logros.exists() else 0
    porcentaje = (puntos_totales / puntos_totales_requeridos) * 100 if puntos_totales_requeridos > 0 else 0

    return render(request, 'bloques_list.html', {
        'bloques': bloques,
        'logros': logros_a_mostrar,
        'puntos_totales': puntos_totales,
        'puntos_totales_requeridos': puntos_totales_requeridos,
        'porcentaje': porcentaje,
    })

def obtener_logros(request):
    actividades = Actividad.objects.filter(realizada=True)
    total_puntos = actividades.aggregate(Sum('puntos'))['puntos__sum'] or 0
    
    logros = Logro.objects.order_by('puntos_necesarios')
    logros_data = []
    
    for logro in logros:
        if logro.puntos_necesarios <= total_puntos:
            estado = 'reached'
        elif logro == logros.filter(puntos_necesarios__gt=total_puntos).first():
            estado = 'next'
        else:
            estado = 'locked'
        
        logros_data.append({
            'nombre': logro.nombre,
            'puntos': logro.puntos_necesarios,
            'estado': estado,
            'descripcion': logro.descripcion,
        })
    
    return JsonResponse({
        'logros': logros_data,
        'total_puntos': total_puntos
    })

def detalle_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    actividades = tema.actividad_set.all().order_by('orden')
    return render(request, 'detalle_tema.html', {'tema': tema, 'actividades': actividades})

def detalle_bloque(request, bloque_id):
    bloque = get_object_or_404(Bloque, id=bloque_id)
    temas = bloque.tema_set.all().order_by('orden')
    return render(request, 'detalle_bloque.html', {'bloque': bloque, 'temas': temas})
