from django.shortcuts import render
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses
import re

from io import BytesIO
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


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
tabela_idade_dados = merge_limpo[['idade','grau','nome_interesse']]
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
alunos_head_html = html_updated = re.sub("class=\"dataframe ", "class=\"", alunos.head(5).to_html(classes='table table-striped',justify='left'))
interesses_head_html = html_updated = re.sub("class=\"dataframe ", "class=\"", interesses.head(5).to_html(classes='table table-striped',justify='left'))
merge_limpo_html = html_updated = re.sub("class=\"dataframe ", "class=\"", merge_limpo.head(5).to_html(classes='table table-striped',justify='left'))
merge_inicial_html = html_updated = re.sub("class=\"dataframe ", "class=\"", merge_inicial.head(5).to_html(classes='table table-striped',justify='left'))
tabela_idade_html = html_updated = re.sub("class=\"dataframe ", "class=\"", tabela_idade.head(30).to_html(classes='table table-striped',justify='left'))
de15_23_html = html_updated = re.sub("class=\"dataframe ", "class=\"", de15_23.head(5).to_html(classes='table table-striped',justify='left'))
de24_32_html = html_updated = re.sub("class=\"dataframe ", "class=\"", de24_32.head(5).to_html(classes='table table-striped',justify='left'))
de33_41_html = html_updated = re.sub("class=\"dataframe ", "class=\"", de33_41.head(5).to_html(classes='table table-striped',justify='left'))
de42_50_html = html_updated = re.sub("class=\"dataframe ", "class=\"", de42_50.head(5).to_html(classes='table table-striped',justify='left'))


## Graficos 
#grafico 15 a 23
de15_23=de15_23.sort_values('grau')
de15_23.plot(kind='barh',figsize=(13,8), color="turquoise")
plt.xlabel('Grau de interesse médio',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.ylabel('Interesses',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.title('Variação de interesses das idade de 15 a 23 anos', 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 22},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png1 = buffer.getvalue()
buffer.close()

de15_23_graphic = base64.b64encode(image_png1)
de15_23_graphic = de15_23_graphic.decode('utf-8')

#grafico 24 a 32
de24_32= de24_32.sort_values('grau')
de24_32.plot(kind='barh',figsize=(10,5), color="turquoise")
plt.xlabel('Grau de interesse médio',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.ylabel('Interesses',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.title('Variação de interesses das idade de 24 a 32 anos', 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 22},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png2 = buffer.getvalue()
buffer.close()

de24_32_graphic = base64.b64encode(image_png2)
de24_32_graphic = de24_32_graphic.decode('utf-8')

#grafico 33 a 41
de33_41= de33_41.sort_values('grau')
de33_41.plot(kind='barh',figsize=(13,8), color="turquoise")
plt.xlabel('Grau de interesse médio',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.ylabel('Interesses',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.title('Variação de interesses das idade de 24 a 32 anos', 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 22},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png3 = buffer.getvalue()
buffer.close()

de33_41_graphic = base64.b64encode(image_png3)
de33_41_graphic = de33_41_graphic.decode('utf-8')

#grafico 42 a 50
de42_50= de42_50.sort_values('grau')
de42_50.plot(kind='barh',figsize=(13,8), color="turquoise")
plt.xlabel('Grau de interesse médio',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.ylabel('Interesses',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.title('Variação de interesses das idade de 24 a 32 anos', 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 22},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png4 = buffer.getvalue()
buffer.close()

de42_50_graphic = base64.b64encode(image_png4)
de42_50_graphic = de42_50_graphic.decode('utf-8')


def analise_raul(request):
    context = {
        'alunos_head': alunos_head_html,
        'interesses_head': interesses_head_html, 
        'merge_inicial' :merge_inicial_html,
        'merge_limpo':merge_limpo_html,
        'tabela_idade':tabela_idade_html,
        'de15_23':de15_23_html,
        'de24_32':de24_32_html,
        'de33_41':de33_41_html,
        'de42_50':de42_50_html,
        'de15_23_graphic':de15_23_graphic,
        'de24_32_graphic':de24_32_graphic,
        'de33_41_graphic':de33_41_graphic,
        'de42_50_graphic':de42_50_graphic,

        
    }
    return render(request, 'raul/main.html', context=context)
