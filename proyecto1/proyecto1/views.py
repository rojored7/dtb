from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader                              #Para cargadores 3
from django.shortcuts import render                             #Para cargadores 4

class Persona(object):
    """docstring for ."""

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #primera vista

    return HttpResponse("Ey RED, I'm back") #responde un texto

def despedida(request):

    return HttpResponse("Ni rendirse")

def adictiva(request):

    fecha_actual=datetime.datetime.now()

    return render(request, "curso1.html",{"tiempo":fecha_actual})

def plant(request):

    p1=Persona("RED","ROJO")
    #nombre = "Red"
    #apellido = "ROJO"
    temas_curso = ["plantillas","Modelos","Formularios","Vistas","Despliegue"]
    ahora=datetime.datetime.now()
    #3 doc_externo=open('C:/Users/REDVAR7/Desktop/py4/django/proyecto1/proyecto1/plantillas/plantilla.html')
    #3 plt=Template(doc_externo.read())
    #3 doc_externo.close()
    #4 doc_externo=loader.get_template('plantilla.html')
    #3 ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"Ahora":ahora,"temas":temas_curso})
    #4 documento = doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"Ahora":ahora,"temas":temas_curso})

    #4 return HttpResponse(documento)
    return render(request, 'plantilla.html',{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"Ahora":ahora,"temas":temas_curso} )
def timers(request):
    fecha_actual=datetime.datetime.now()

    documento="""Fecha y hora %s""" % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request,edad, agno):

    #edadActual = 18
    periodo =agno-2019
    edadFutura = edad+periodo
    documento1  ="""<html><body><h2>En el año %s tendras %s años</h2></body></html>"""%(agno,edadFutura)
    return HttpResponse(documento1)
