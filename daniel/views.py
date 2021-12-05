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

data = merge_inicial[['id_interesse','categoria','nome_interesse','grau']]

###Analises
#fazendo a tabela relacionado idade com os interesses
data = data[['nome_interesse','grau']]
data_soma_interesse= data.groupby(['nome_interesse']).sum().sort_values(['grau'],ascending=False)

data_soma_interesse_graf=data_soma_interesse.sort_values('grau')

##Separando a tabela por grupos de idades

# Preparando dataframes que serão mostrados.
alunos_head_html = html_updated = re.sub("class=\"dataframe ", "class=\"", alunos.head(5).to_html(classes='table table-striped',justify='left'))
interesses_head_html = html_updated = re.sub("class=\"dataframe ", "class=\"", interesses.head(5).to_html(classes='table table-striped',justify='left'))
data_html = html_updated = re.sub("class=\"dataframe ", "class=\"", data.head(5).to_html(classes='table table-striped',justify='left'))
data_soma_interesse_html = html_updated = re.sub("class=\"dataframe ", "class=\"", data_soma_interesse.head(10).to_html(classes='table table-striped',justify='left'))


## Graficos 
data_soma_interesse_graf.plot(kind='barh',figsize=(13,16), color="turquoise")
plt.xlabel('Nivel de interesse',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.ylabel('Interesses',          
           fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.title('Visão geral dos interesses', 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 22},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

data_soma_interesse_graf = base64.b64encode(image_png)
data_soma_interesse_graf = data_soma_interesse_graf.decode('utf-8')


def analise_daniel(request):
    context = {
        'alunos_head': alunos_head_html,
        'interesses_head': interesses_head_html, 
        'data' :data_html,
        'data_soma_interesse':data_soma_interesse_html,
        'data_soma_interesse_graf':data_soma_interesse_graf,

        
    }
    return render(request, 'daniel/main.html', context=context)
