from django.shortcuts import render
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses

alunos = Aluno.objects
interesses = Interesses.objects
alunos_interesses = Aluno_Interesses.objects

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

#Mergeando
df = alunos_df.merge(alunos_interesses_df, left_on='id', right_on='aluno_id_id').merge(interesses_df, left_on='interesses_id_id', right_on="id")

#Filtrando
df_filtrado = df.query(f'nome_y in {interesses_saudaveis}')
df_filtrado_grau = pd.DataFrame(df_filtrado.loc[df_filtrado['grau'] >= 3])        

#Calculando os unique
unique_filtrado = pd.unique(df_filtrado_grau['aluno_id_id'])
unique_original = pd.unique(df['aluno_id_id'])

#Calculando porcentagem
porcentagem = (len(unique_filtrado)/len(unique_original))*100

def eda(request):
    context = {
        'alunos': lista_alunos[0:20],
        'interesses': lista_interesses[0:20],
        'interesses_distinct': interesses_distintos,
        'interesses_saudaveis': interesses_saudaveis,
        'aluno_interesses_df': df.values.tolist()[0:20],
        'df_filtrado': df_filtrado_grau.values.tolist()[0:20],
        'tamanho_filtrado': len(unique_filtrado),
        'tamanho_original': len(unique_original),
        'porcentagem': round(porcentagem, 2)
    }
    return render(request, 'cristiano/eda.html', context=context)
