from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()
    turnos = (
        (1, 'Manana'),
        (2, 'Tarde'),
        (3, 'Noche')
    )
    turno = models.PositiveSmallIntegerField(choices = turnos, null = True)


class Instructor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cursos_asignados = models.IntegerField()
