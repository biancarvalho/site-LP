from django.db import models

class Interesses(models.Model):
    categoria = models.CharField(max_length=80) 
    grau = models.IntegerField()
    nome = models.CharField(max_length=80)

class Aluno(models.Model):
    nome = models.CharField(max_length=80)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    curso = models.CharField(max_length=80)
    periodo = models.IntegerField()
    interesses = models.ManyToManyField(Interesses, null=True)    