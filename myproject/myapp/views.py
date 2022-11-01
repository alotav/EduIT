# Create your views here.
import csv
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

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

def aeropuertos(request):
    f = open(r"C:\Users\Alonso\Desktop\Educacion IT\EduIT-Django\Descargas\aeropuertos.csv", encoding="utf8")
    html = """
        <html>
        <title>Lista de aeropuertos</title>
        <table style="border: 1px solid">
          <thead>
            <tr>
              <th>Aeropuerto</th>
              <th>Ciudad</th>
              <th>País</th>
            </tr>
          </thead>
    """
    for linea in f:
        datos = linea.split(",")
        nombre = datos[1].replace('"', "")
        ciudad = datos[2].replace('"', "")
        pais = datos[3].replace('"', "")
        html += f"""
            <tr>
              <td>{nombre}</td>
              <td>{ciudad}</td>
              <td>{pais}</td>
            </tr>
        """
    f.close()
    html += "</table></html>"
    return HttpResponse(html)


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