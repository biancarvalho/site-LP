from django.shortcuts import render
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses
import re



alunos = Aluno.objects.all().values()
interesses = Interesses.objects.all().values()
alunos_interesses = Aluno_Interesses.objects.all().values()

alunos = pd.DataFrame(alunos)
interesses = pd.DataFrame(interesses)
alunos_interesses = pd.DataFrame(alunos_interesses)

#Mergeando
merge_inicial = alunos.merge(alunos_interesses, left_on='id', right_on='aluno_id_id').merge(interesses, left_on='interesses_id_id', right_on="id")
merge_inicial = merge_inicial.rename(columns={'id_x': 'id_aluno', 'nome_x': 'nome_aluno', 'id_y':'id_interesse','id_y':'id_aluno_interesse','id':'id_interesse','nome_y':'nome_interesse'})

merge_limpo =merge_inicial[['id_aluno_interesse','id_aluno','id_interesse','nome_aluno','idade','categoria','nome_interesse','grau']]


###Começando analise de verdade
#fazendo a tabela relacionado idade com os interesses
tabela_idade_dados=merge_limpo[['idade','grau','nome_interesse']]
tabela_idade = tabela_idade_dados.groupby(['idade','nome_interesse']).mean().sort_values(['idade','grau'],ascending=False)

##Separando a tabela por grupos de idades
#Tabela de interesses de pessoas de 15 a 23 anos  
de15_23= tabela_idade_dados[tabela_idade_dados['idade']>=15]
de15_23= de15_23[de15_23['idade']<=23]
de15_23=de15_23.groupby(['nome_interesse']).mean().sort_values(['grau'],ascending=False)
de15_23=de15_23.drop(columns=['idade'])

#Tabela de interesses de pessoas de 24 a 32 anos  
de24_32= tabela_idade_dados[tabela_idade_dados['idade']>=24]
de24_32= de24_32[de24_32['idade']<=32]
de24_32=de24_32.groupby(['nome_interesse']).mean().sort_values(['grau'],ascending=False)
de24_32=de24_32.drop(columns=['idade'])

#Tabela de interesses de pessoas de 33 a 41 anos  
de33_41= tabela_idade_dados[tabela_idade_dados['idade']>=33]
de33_41= de33_41[de33_41['idade']<=41]
de33_41=de33_41.groupby(['nome_interesse']).mean().sort_values(['grau'],ascending=False)
de33_41=de33_41.drop(columns=['idade'])

#Tabela de interesses de pessoas de 42 a 50 anos  
de42_50= tabela_idade_dados[tabela_idade_dados['idade']>=42]
de42_50= de42_50[de42_50['idade']<=50]
de42_50=de42_50.groupby(['nome_interesse']).mean().sort_values(['grau'],ascending=False)
de42_50=de42_50.drop(columns=['idade'])

# Preparando dataframes que serão mostrados.
alunos_head = html_updated = re.sub("class=\"dataframe ", "class=\"", alunos.head(5).to_html(classes='table table-striped',justify='left'))
interesses_head = html_updated = re.sub("class=\"dataframe ", "class=\"", interesses.head(5).to_html(classes='table table-striped',justify='left'))
merge_limpo = html_updated = re.sub("class=\"dataframe ", "class=\"", merge_limpo.head(5).to_html(classes='table table-striped',justify='left'))
merge_inicial = html_updated = re.sub("class=\"dataframe ", "class=\"", merge_inicial.head(5).to_html(classes='table table-striped',justify='left'))
tabela_idade = html_updated = re.sub("class=\"dataframe ", "class=\"", tabela_idade.head(30).to_html(classes='table table-striped',justify='left'))
de15_23 = html_updated = re.sub("class=\"dataframe ", "class=\"", de15_23.head(5).to_html(classes='table table-striped',justify='left'))
de24_32 = html_updated = re.sub("class=\"dataframe ", "class=\"", de24_32.head(5).to_html(classes='table table-striped',justify='left'))
de33_41 = html_updated = re.sub("class=\"dataframe ", "class=\"", de33_41.head(5).to_html(classes='table table-striped',justify='left'))
de42_50 = html_updated = re.sub("class=\"dataframe ", "class=\"", de42_50.head(5).to_html(classes='table table-striped',justify='left'))

def analise_raul(request):

    context = {
        'alunos_head': alunos_head,
        'interesses_head': interesses_head, 
        'merge_inicial' :merge_inicial,
        'merge_limpo':merge_limpo,
        'tabela_idade':tabela_idade,
        'de15_23':de15_23,
        'de24_32':de24_32,
        'de33_41':de33_41,
        'de42_50':de42_50,

        
    }
    return render(request, 'raul/main.html', context=context)
