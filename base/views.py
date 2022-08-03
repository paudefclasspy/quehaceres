from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def tarea(request):
    return HttpResponse("Hola que tal")