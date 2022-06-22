from tkinter import CASCADE
from django.db import models

# Create your models here.
class Sexo(models.Model):
	sexo = models.CharField(max_length=15)
	
class Personaje(models.Model):
    nombre = models.CharField(max_length=120)
    sexo = models.ForeignKey(Sexo,null=False,on_delete=models.PROTECT)