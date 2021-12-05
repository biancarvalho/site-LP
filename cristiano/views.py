from django.shortcuts import render
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses
from sylvio import views as base_analise
import re


interesses_distintos = base_analise.interesses.values('nome').distinct()
interesses_saudaveis = ['Dança',
'Volei', 'Futebol', 'Handbol', 'Basquete',
'Tenis de Mesa', 'Natação', 'Crossfit', 'Musculação',
'Golfe', 'Passeio no Parque', 'Trilhas', 'Montanhas']

#Mergeando
df = base_analise.alunos_df.merge(base_analise.alunos_interesses_df, left_on='id', right_on='aluno_id_id').merge(base_analise.interesses_df, left_on='interesses_id_id', right_on="id")

#Filtrando
df_filtrado = df.query(f'nome_y in {interesses_saudaveis}')
df_filtrado_grau = pd.DataFrame(df_filtrado.loc[df_filtrado['grau'] >= 3])        

#Calculando os unique
unique_filtrado = pd.unique(df_filtrado_grau['aluno_id_id'])
unique_original = pd.unique(df['aluno_id_id'])

#Calculando porcentagem
porcentagem = (len(unique_filtrado)/len(unique_original))*100


df_filtrado = html_updated = re.sub("class=\"dataframe ", "class=\"", df_filtrado.head(10).to_html(classes='table table-striped',justify='left', index=True))


def eda(request):
    context = {
        'alunos': base_analise.lista_alunos[0:10],
        'interesses': base_analise.lista_interesses[0:10],
        'interesses_distinct': interesses_distintos,
        'interesses_saudaveis': interesses_saudaveis,
        'aluno_interesses_df': df.values.tolist()[0:10],
        'df_filtrado': df_filtrado,
        'tamanho_filtrado': len(unique_filtrado),
        'tamanho_original': len(unique_original),
        'porcentagem': round(porcentagem, 2),
        'df': base_analise.df,
    }
    return render(request, 'cristiano/main.html', context=context)
