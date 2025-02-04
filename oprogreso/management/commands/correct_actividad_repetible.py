from django.core.management.base import BaseCommand
from oprogreso.models import Actividad

class Command(BaseCommand):
    help = 'set veces realizado = 1 where realizado = true'

    def handle(self, *args, **kwargs):
        
        Actividad.objects.filter(realizada=True).update(veces_realizada=1)
        
        Actividad.objects.filter(titulo='Podcast').update(repetible=True)
        

        self.stdout.write(self.style.SUCCESS('Actividades actualizadas exitosamente.'))
