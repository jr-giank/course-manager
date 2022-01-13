from django.db import models
from django.db.models.base import Model

# Create your models here.

class Cursos(models.Model):

    creditos = models.IntegerField(blank=False, null=True)
    nombre_asignatura = models.TextField(max_length=45, blank=False)
    costo = models.DecimalField(max_digits=10, decimal_places=8, null=True)

    def __str__(self):

        return self.nombre_asignatura