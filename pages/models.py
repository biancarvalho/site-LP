from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=80)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    curso = models.CharField()
    periodo = models.IntegerField()
    interesses = models.CharField()

class Interesses(models.Model):
    categoria = models.CharField() 
    grau = models.IntegerField()
    nome = models.CharField()