from django.shortcuts import render , HttpResponse , HttpResponseRedirect
import requests
import json


# Create your views here.

def Home(request):
    return render(request, "home.html",{'form':consulta_Api_Usuario()})
def api_Organismos(request):
    return render(request, "organismos.html", {'form' :consulta_Api_Organismos()})
def api_Programas(request):
    return render(request, "programas.html",{'form' :consulta_Api_Programas()})
def api_Museos(request):
    return render(request, "museos.html",{'form' :consulta_Api_Museos()})
def api_Institutos(request):
    return render(request, "institutos.html",{'form' :consulta_Api_Institutos()})
def api_Tramites(request):
    return render(request, "tramites.html",{'form' :consulta_Api_Tramites()})

def api_Convocatorias(request):
    return render(request, "convocatorias.html",{'form' :consulta_Api_Convocatorias()})


    
# # #-------------------- Apis que Utilizo consultas:---------------
# o	Resultados:
# 	"organismos": "https://www.cultura.gob.ar/api/v2.0/organismos/?format=json",
# 	"programas": "https://www.cultura.gob.ar/api/v2.0/programas/?format=json",
# 	"museos": "https://www.cultura.gob.ar/api/v2.0/museos/?format=json",
# 	"institutos": "https://www.cultura.gob.ar/api/v2.0/institutos/?format=json",
# 	"tramites": "https://www.cultura.gob.ar/api/v2.0/tramites/?format=json",
# 	"convocatorias": https://www.cultura.gob.ar/api/v2.0/convocatorias/?format=json


def consulta_Api_Usuario():
    reponse= requests.get("https://www.cultura.gob.ar/api/v2.0/usuarios/?format=json")
    if reponse.status_code == 200:
        respuestaApi=reponse.json()
        return respuestaApi

def consulta_Api_Organismos():
    reponse= requests.get("https://www.cultura.gob.ar/api/v2.0/organismos/?format=json")
    if reponse.status_code == 200:
        respuestaApi=reponse.json()
        format = respuestaApi['results']
        format_doc = {}
        cont=0
        for i in format:
            format_doc[cont]=i
            cont+=1
        return format_doc
def consulta_Api_Programas():
    reponse= requests.get("https://www.cultura.gob.ar/api/v2.0/programas/?format=json")
    if reponse.status_code == 200:
        respuestaApi=reponse.json()
        format = respuestaApi['results']
        format_doc = {}
        cont=0
        for i in format:
            format_doc[cont]=i
            cont+=1
        return format_doc

def consulta_Api_Museos():
    reponse= requests.get("https://www.cultura.gob.ar/api/v2.0/museos/?format=json")
    if reponse.status_code == 200:
        respuestaApi=reponse.json()
        format = respuestaApi['results']
        format_doc = {}
        cont=0
        for i in format:
            format_doc[cont]=i
            cont+=1
        return format_doc

def consulta_Api_Institutos():
    reponse= requests.get("https://www.cultura.gob.ar/api/v2.0/institutos/?format=json")
    if reponse.status_code == 200:
        respuestaApi=reponse.json()
        format = respuestaApi['results']
        format_doc = {}
        cont=0
        for i in format:
            format_doc[cont]=i
            cont+=1
        return format_doc

def consulta_Api_Tramites():
    reponse= requests.get("https://www.cultura.gob.ar/api/v2.0/tramites/?format=json")
    if reponse.status_code == 200:
        respuestaApi=reponse.json()
        format = respuestaApi['results']
        format_doc = {}
        cont=0
        for i in format:
            format_doc[cont]=i
            cont+=1
        return format_doc

def consulta_Api_Convocatorias():
    reponse= requests.get("https://www.cultura.gob.ar/api/v2.0/convocatorias/?format=json")
    if reponse.status_code == 200:
        respuestaApi=reponse.json()
        format = respuestaApi['results']
        format_doc = {}
        cont=0
        for i in format:
            format_doc[cont]=i
            cont+=1
        return format_doc

