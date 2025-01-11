from django.db import models

class Bloque(models.Model):
    titulo = models.CharField(max_length=200)
    orden = models.IntegerField(default=0)  # Field for ordering

    def __str__(self):
        return self.titulo

class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(null=True, blank=True)
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE)  # Linking Tema to Bloque
    notas = models.TextField(blank=True)
    orden = models.IntegerField(default=0)  # Field for ordering

    def __str__(self):
        return self.titulo

class Actividad(models.Model):
    titulo = models.CharField(max_length=200)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)  # Linking Actividad to Tema
    puntos = models.IntegerField(default=0)
    realizada = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)  # Field for date
    orden = models.IntegerField(default=0)  # Field for ordering

    def __str__(self):
        return f"Actividad for {self.tema.titulo} - Puntos: {self.puntos}"

class Logro(models.Model):
    nombre = models.CharField(max_length=255)
    puntos_necesarios = models.IntegerField(default=0)  # Puntos necesarios para alcanzar el logro
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)  # Field to indicate completion

    def __str__(self):
        return self.nombre
