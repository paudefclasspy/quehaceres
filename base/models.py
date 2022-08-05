from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField(max_length=400,blank=True)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title