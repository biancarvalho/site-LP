from django.shortcuts import render
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses

alunos = Aluno.objects
interesses = Interesses.objects
alunos_interesses = Interesses.objects

lista_alunos = alunos.values()
lista_interesses = interesses.values()
lista_alunos_interesses = alunos_interesses.values()

interesses_distintos = interesses.values('nome').distinct()
interesses_saudaveis = ['Dança',
'Volei', 'Futebol', 'Handbol', 'Basquete',
'Tenis de Mesa', 'Natação', 'Crossfit', 'Musculação',
'Golfe', 'Passeio no Parque', 'Trilhas', 'Montanhas']


alunos_df = pd.DataFrame(lista_alunos)
interesses_df = pd.DataFrame(lista_interesses)
alunos_interesses_df = pd.DataFrame(lista_alunos_interesses)

#alunos_df = alunos_df.merge(alunos_interesses_df, left_on='id', right_on='aluno_id_id')




def eda(request):
    context = {
        'alunos': lista_alunos[0:20],
        'interesses': lista_interesses[0:20],
        'interesses_distinct': interesses_distintos,
        'interesses_saudaveis': interesses_saudaveis,
        #'aluno_df': alunos_df
    }
    return render(request, 'cristiano/eda.html', context=context)
