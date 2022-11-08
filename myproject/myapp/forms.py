from django import forms

class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    inscriptos = forms.IntegerField(label="Inscriptos")
    turnos = (
        (1, "Manana"),
        (2, "Tarde"),
        (3, "Noche")
    )
    turno = forms.ChoiceField(label='Turno', choices=turnos)


class FormularioPeliculas(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=128)
    fecha_estreno = forms.DateField(label='Fecha de Estreno', widget=forms.DateInput(attrs={'type': 'date'}))
    publico = forms.IntegerField(label='Para mayores de:')
    preventa = forms.BooleanField(label='Preventa online?', required=False)