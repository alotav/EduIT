# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from . import forms
import sqlite3
from django.http import HttpResponseRedirect
from django.urls import reverse



# MODELS:
from .models import Curso, Instructor



def index(request):
    return render(request, "myapp/index.html")

def dolar(request):

    # Importamos requests y consultamos a la api dolar:
    req = requests.get('https://api.recursospython.com/dollar')
    # Convertimos a json la consulta:
    req = req.json()
    # Accedemos a los valores como si se tratase de un diccionario ya que el json tiene el mismo formato:
    compra = req['buy_price']
    venta = req['sale_price']
        
    # Pasamos los valores de las variables a la plantilla por diccionario:
    return render(request, "myapp/cotizacion-dolar.html", {'compra':compra, 'venta': venta})

# DESAFIO 1:

# def aeropuertos(request):
#     f = open(r"C:\Users\Alonso\Desktop\Educacion IT\EduIT-Django\Descargas\aeropuertos.csv", encoding="utf8")
#     html = """
#         <html>
#         <title>Lista de aeropuertos</title>
#         <table style="border: 1px solid">
#           <thead>
#             <tr>
#               <th>Aeropuerto</th>
#               <th>Ciudad</th>
#               <th>País</th>
#             </tr>
#           </thead>
#     """
#     for linea in f:
#         datos = linea.split(",")
#         nombre = datos[1].replace('"', "")
#         ciudad = datos[2].replace('"', "")
#         pais = datos[3].replace('"', "")
#         html += f"""
#             <tr>
#               <td>{nombre}</td>
#               <td>{ciudad}</td>
#               <td>{pais}</td>
#             </tr>
#         """
#     f.close()
#     html += "</table></html>"
#     return HttpResponse(html)

# DESAFIO 2:

def aeropuertos(request):
    f = open(r"C:\Users\Alonso\Desktop\Educacion IT\EduIT-Django\Descargas\aeropuertos.csv", encoding="utf8")
    aero = []
    for linea in f:
        datos = linea.split(",")
        nombre = datos[1].replace('"', "")
        ciudad = datos[2].replace('"', "")
        pais = datos[3].replace('"', "")
        
        aero.append([nombre,ciudad,pais])
        
    f.close()
    # print (aero)
    # print()
    # for n, c, p in aero:
    #     print(f'Nombre: {n} Ciudad: {c} Pais: {p} \n',)
    return render(request, 'myapp/aeropuertos.html', {'aero': aero})




def aeropuertos_json(request):
    f = open(r"C:\Users\Alonso\Desktop\Educacion IT\EduIT-Django\Descargas\aeropuertos.csv", encoding="utf8")
    aeropuertos = []
    for linea in f:
        datos = linea.split(",")
        aeropuerto = {
            "nombre": datos[1].replace('"', ""),
            "ciudad": datos[2].replace('"', ""),
            "pais": datos[3].replace('"', "")
        } 
        aeropuertos.append(aeropuerto)
        
    print(aeropuertos)
    f.close()
    return JsonResponse(aeropuertos, safe=False)


# def cursos(request):
#     conn = sqlite3.connect("cursos.sqlite3")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM cursos")
#     query = cursor.fetchall()
#     conn.close()
#     return render(request, 'myapp/cursos.html', {'query': query})

def cursos(request):
    cursos = Curso.objects.all()
    ctx = {'cursos':cursos}
    for c in cursos:
        print(f"Nombre: {c.nombre}\nInscriptos: {c.inscriptos}")
    return render(request, 'myapp/cursos.html', ctx)



# TOMANDO EL FORMULARIO CREADO DIRECTAMENTE DESDE FORMS.PY:
# def nuevo_curso(request):
#     if request.method == "POST":
#         form = forms.FormularioCurso(request.POST)
#         if form.is_valid():
#             conn = sqlite3.connect("cursos.sqlite3")
#             cursos = conn.cursor()
#             cursos.execute("CREATE TABLE IF NOT EXISTS CURSOS(nombre CHAR(50) NOT NULL,cursos INTEGER NOT NULL)")
#             cursos.execute("INSERT INTO cursos VALUES (?, ?)" , (form.cleaned_data["nombre"], form.cleaned_data["inscriptos"]) )
#             conn.commit()
#             conn.close()
#             return HttpResponseRedirect(reverse("cursos"))
#     else:
#         form = forms.FormularioCurso()
#     ctx = {"form": form}
#     return render(request, "myapp/nuevo_curso.html", ctx)



# USANDO FORMULARIO QUE HEREDA DESDE MODELS: AL HEREDAR DE MODELS, AHORA LOS CAMBIOS SE GUARDAN CON LA FUNCION save():
def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormDesdeModelCurso(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormDesdeModelCurso()
    ctx = {"form": form}
    return render(request, "myapp/nuevo_curso.html", ctx)


def turno_manana(request):
    consulta = Curso.objects.filter(turno = 1)
    # for c in consulta:
    #     print(c.nombre)
    return render(request, "myapp/turno_manana.html", {'consulta':consulta})
 
def turno_tarde(request):
    consulta = Curso.objects.filter(turno = 2)
    return render(request, "myapp/turno_tarde.html", {'consulta':consulta})

def turno_noche(request):
    consulta = Curso.objects.filter(turno = 3)
    return render(request, "myapp/turno_noche.html", {'consulta':consulta})


def nueva_pelicula(request):
    if request.method == "POST":
        form = forms.FormularioPeliculas(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            conn = sqlite3.connect("peliculas.sqlite3")
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS peliculas (nombre CHAR(50) NOT NULL, fecha_estreno DATE NOT NULL, edad INTEGER NOT NULL, preventa BOOLEAN)")
            # print((form.cleaned_data["nombre"], form.cleaned_data["fecha_estreno"], form.cleaned_data["publico"], form.cleaned_data["preventa"]))
            cursor.execute("INSERT INTO peliculas VALUES (?, ?, ?, ?)", (form.cleaned_data['nombre'], form.cleaned_data['fecha_estreno'], form.cleaned_data['publico'], form.cleaned_data['preventa']))
            conn.commit()
            conn.close()
            return render(request, 'myapp/pelicula_agregada.html', {'form':form.cleaned_data})
            
        else:
            print('form invalido')
    else:
        form = forms.FormularioPeliculas()

    return render(request, 'myapp/nueva_pelicula.html', {'form':form})


def agregar_instructores(request):
    if request.method == 'POST':
        formu = forms.FormularioInstructor(request.POST)
        if formu.is_valid():
            # print(formu.cleaned_data)
            Instructor.objects.create(
                nombre = formu.cleaned_data['nombre'],
                email = formu.cleaned_data['email'],
                cursos_asignados = formu.cleaned_data['cursos_asignados']
            )

            return redirect('instructores')
    else:
        formu = forms.FormularioInstructor()
        return render(request, 'myapp/form_instructores.html', {'formu':formu})



def instructores(request):
    instructores = Instructor.objects.all()
    print (instructores)
    return render(request, 'myapp/instructores.html', {'instructores':instructores})