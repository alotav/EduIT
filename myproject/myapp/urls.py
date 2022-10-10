# creamos urls.py y agregamos las siguientes lineas

from django.urls import path
from . import views


urlpatterns = [
    path('myapp/',views.index, name = "index"),
]