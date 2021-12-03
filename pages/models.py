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

class Aluno_Interesses(models.Model):
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    interesses_id = models.ForeignKey(Interesses, on_delete=models.CASCADE)

class Perguntas(models.Model):
    slug = models.SlugField(max_length=255,unique=True)
    pergunta = models.CharField(max_length=255)
    alternativa1 = models.CharField(max_length=255)
    alternativa2 = models.CharField(max_length=255)
    alternativa3 = models.CharField(max_length=255)
    alternativa4 = models.CharField(max_length=255)
    alternativa5 = models.CharField(max_length=255)
    
    def __str__(self):
        return self.slug