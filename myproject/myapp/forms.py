from django import forms

# Para crear formulario a partir de un modelo:
from django.forms import ModelForm
from .models import Curso

# class FormularioCurso(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=128)
#     inscriptos = forms.IntegerField(label="Inscriptos")
#     turnos = (
#         (1, "Manana"),
#         (2, "Tarde"),
#         (3, "Noche")
#     )
#     turno = forms.ChoiceField(label='Turno', choices=turnos)

class FormDesdeModelCurso(ModelForm):
    class Meta: 
        model = Curso
        fields = ("nombre", "inscriptos", "turno")


class FormularioPeliculas(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=128)
    fecha_estreno = forms.DateField(label='Fecha de Estreno', widget=forms.DateInput(attrs={'type': 'date'}))
    publico = forms.IntegerField(label='Para mayores de:')
    preventa = forms.BooleanField(label='Preventa online?', required=False)



class FormularioInstructor(forms.Form):
    nombre = forms.CharField(label= 'Nombre',max_length=50)
    email = forms.EmailField(label='Email')
    cursos_asignados = forms.IntegerField(label='Cursos Asignados')