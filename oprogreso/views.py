from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import Bloque, Tema, Actividad

def homepage(request):
    bloques = Bloque.objects.all().order_by('orden')
    return render(request, 'home.html', {'bloques': bloques})

def about(request):
    return render(request, 'about.html')

def marcar_actividad(request, actividad_id):
    if request.method == 'POST':
        actividad = get_object_or_404(Actividad, id=actividad_id)
        actividad.realizada = True
        actividad.fecha = timezone.now()
        actividad.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
