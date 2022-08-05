from asyncio import tasks
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarea
from django.views.generic.list import ListView

class ListaTarea(ListView):
    model = Tarea

    