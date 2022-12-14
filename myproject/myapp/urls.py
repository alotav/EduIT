# creamos urls.py y agregamos las siguientes lineas

from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name = "index"),
    path('cotizacion-dolar',views.dolar, name = "dolar"),
    path('aeropuertos',views.aeropuertos, name = "aeropuertos"),
    path('aeropuertosjson',views.aeropuertos_json, name = "aeropuertosjson"),
    path('cursos',views.cursos, name = "cursos"),
    path('nuevo_curso',views.nuevo_curso, name = "nuevo_curso"),
    path('nueva_pelicula',views.nueva_pelicula, name = "nueva_pelicula"),
    path('instructores',views.instructores, name = "instructores"),
    path('agregar_instructores',views.agregar_instructores, name = "agregar_instructores"),
    path('turno_manana',views.turno_manana, name = "turno_manana"),
    path('turno_tarde',views.turno_tarde, name = "turno_tarde"),
    path('turno_noche',views.turno_noche, name = "turno_noche")
]