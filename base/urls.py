from django.urls import path
from .views import ListaTarea, TareaDetail

urlpatterns = [
    path('', ListaTarea.as_view(), name='tareas'),
    path('tarea/<int:pk>/', TareaDetail.as_view(), name='tarea'),
]