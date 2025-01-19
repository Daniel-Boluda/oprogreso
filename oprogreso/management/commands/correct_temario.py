from django.core.management.base import BaseCommand
from oprogreso.models import Tema

class Command(BaseCommand):
    help = 'Actualizar temas con orden >= 12'

    def handle(self, *args, **kwargs):
        # Obtener todos los temas con orden >= 12
        temas = Tema.objects.filter(orden__gte=12)

        # Iterar sobre los temas seleccionados
        for tema in temas:
            # Concatenar el título y el contenido
            nuevo_contenido = f"{tema.titulo} {tema.contenido}"

            # Actualizar los campos de título y contenido
            tema.titulo = f"Tema {tema.orden}"
            tema.contenido = nuevo_contenido
            tema.save()

        self.stdout.write(self.style.SUCCESS('Temas actualizados exitosamente.'))
