from django.contrib import admin
from .models import Aluno, Interesses, Perguntas, ranking

admin.site.register(Aluno)
admin.site.register(Interesses)
admin.site.register(Perguntas)
admin.site.register(ranking)