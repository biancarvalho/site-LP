from django.shortcuts import render
import pandas as pd
from pages.models import *
import re
from io import BytesIO
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

alunos = Aluno.objects.all().values()
interesses = Interesses.objects.all().values()
alunos_interesses = Aluno_Interesses.objects.all().values()

alunos = pd.DataFrame(alunos)
interesses = pd.DataFrame(interesses)
alunos_interesses = pd.DataFrame(alunos_interesses)

#Mergeando
merge_inicial = alunos.merge(alunos_interesses, left_on='id', right_on='aluno_id_id').merge(interesses, left_on='interesses_id_id', right_on="id")
merge_inicial = merge_inicial.rename(columns={'id_x': 'id_aluno', 'nome_x': 'nome_aluno', 'id_y':'id_interesse','id_y':'id_aluno_interesse','id':'id_interesse','nome_y':'nome_interesse'})

df = merge_inicial[['id_aluno_interesse','id_aluno','id_interesse','nome_aluno','sexo','idade','categoria','nome_interesse','grau']]

# Filtrando os dados
df_sexo = df[['sexo','grau','nome_interesse','categoria']]

##Separando a tabela pelo sexo
#Tabela de interesses de pessoas do sexo feminino  
df_f = df_sexo[df_sexo['sexo']=='F']

#Tabela de interesses de pessoas do sexo mascFalulino  
df_m = df_sexo[df_sexo['sexo']=='M']


## Graficos 

#grafico sexo feminino
plt.figure(figsize=(11,6))
sns.violinplot(data=df, x="grau", y="categoria", hue="sexo",
               split=True, inner="quart", linewidth=1, palette='bright')

plt.xlabel('Grau de interesse',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.ylabel('Interesses',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.title('Variação de interesses do sexo feminino', 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 20},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

grafico1 = base64.b64encode(image_png)
grafico1 = grafico1.decode('utf-8')

#grafico sexo masculino
plt.rcParams.update({'font.family': 'serif',
                    'font.size': 8})

plt.figure(figsize=(11,9))                    
sns.boxplot(x='grau', y='nome_interesse', data=df_m)

plt.xlabel('Grau de interesse',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.ylabel('Interesses',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.title('Variação de interesses do sexo masculino', 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 20},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

grafico2 = base64.b64encode(image_png)
grafico2 = grafico2.decode('utf-8')

#grafico sexo feminino
plt.rcParams.update({'font.family': 'serif',
                    'font.size': 8})

plt.figure(figsize=(11,9))                    
sns.boxplot(x='grau', y='nome_interesse', data=df_f)

plt.xlabel('Grau de interesse',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.ylabel('Interesses',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.title('Variação de interesses do sexo masculino', 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 20},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

grafico3 = base64.b64encode(image_png)
grafico3 = grafico3.decode('utf-8')


# Preparando dataframes que serão mostrados.
alunos_head = html_updated = re.sub("class=\"dataframe ", "class=\"", alunos.head(5).to_html(classes='table table-striped',justify='left'))
interesses_head = html_updated = re.sub("class=\"dataframe ", "class=\"", interesses.head(5).to_html(classes='table table-striped',justify='left'))
df = html_updated = re.sub("class=\"dataframe ", "class=\"", df.head(5).to_html(classes='table table-striped',justify='left'))
df_m = html_updated = re.sub("class=\"dataframe ", "class=\"", df_m.head(5).to_html(classes='table table-striped',justify='left'))
df_f = html_updated = re.sub("class=\"dataframe ", "class=\"", df_f.head(5).to_html(classes='table table-striped',justify='left'))


def analises_bianca(request):
    context = {
        'alunos_head': alunos_head,
        'interesses_head': interesses_head, 
        'merge_inicial': merge_inicial,
        'df': df,
        'df_f': df_f,
        'df_m': df_m,
        'grafico1': grafico1,
        'grafico2': grafico2,
        'grafico3': grafico3,
    }
    return render(request, 'bianca/main.html', context=context)
