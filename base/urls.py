from django.urls import path
from .views import ListaTarea

urlpatterns = [
    path('', ListaTarea.as_view(),name="tareas"),
]