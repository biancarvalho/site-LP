from django.shortcuts import render 
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses
import re

from io import BytesIO
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 12,
                            'font.family': 'sans-serif'})

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

por_curso = merge_inicial[['curso','categoria','nome_interesse','grau']]

CD=por_curso[por_curso['curso']=='Ciência de Dados e Inteligência Artificial']
CD=CD[['nome_interesse','grau']]
CD_gb= CD.groupby(['nome_interesse']).sum().sort_values(['grau'],ascending=False)

CD_gb_graf=CD_gb.sort_values('grau',ascending=True)

MAT=por_curso[por_curso['curso']=='Matemática Aplicada']
MAT=MAT[['nome_interesse','grau']]
MAT_gb= MAT.groupby(['nome_interesse']).sum().sort_values(['grau'],ascending=False)

MAT_gb_graf=MAT_gb.sort_values('grau',ascending=True)

MAT_gb_ord=MAT_gb.sort_values(['nome_interesse'])
CD_gb_ord=CD_gb.sort_values(['nome_interesse'])

CD_MAT = CD_gb_ord.merge(MAT_gb_ord, left_on='nome_interesse', right_on='nome_interesse')
CD_MAT=CD_MAT.rename(columns={'grau_x': 'grau_CD','grau_y':'grau_MAT'})
CD_MAT['soma'] = CD_MAT.sum(axis=1)
CD_MAT=CD_MAT.sort_values(['soma'],ascending=False)

CD_MAT_graf=CD_MAT.head(10)
CD_MAT_graf=CD_MAT_graf.sort_values(['soma'],ascending=True)

# Preparando dataframes que serão mostrados.
alunos_head_html  = re.sub("class=\"dataframe ", "class=\"", alunos.head(5).to_html(classes='table table-striped',justify='left'))
interesses_head_html  = re.sub("class=\"dataframe ", "class=\"", interesses.head(5).to_html(classes='table table-striped',justify='left'))
data_html  = re.sub("class=\"dataframe ", "class=\"", data.head(5).to_html(classes='table table-striped',justify='left'))
data_soma_interesse_html = re.sub("class=\"dataframe ", "class=\"", data_soma_interesse.head(5).to_html(classes='table table-striped',justify='left'))
CD_gb_html =  re.sub("class=\"dataframe ", "class=\"", CD_gb.head(5).to_html(classes='table table-striped',justify='left'))
MAT_gb_html = re.sub("class=\"dataframe ", "class=\"", MAT_gb.head(5).to_html(classes='table table-striped',justify='left'))
CD_MAT_html = re.sub("class=\"dataframe ", "class=\"", CD_MAT.head(5).to_html(classes='table table-striped',justify='left'))

## Graficos 
MAT_gb_graf.plot(kind='barh',figsize=(15,12), color="orange")
plt.xlabel('Nivel de interesse')
plt.ylabel('Interesses')
plt.title('Visão geral dos interesses dos alunos de MAp', loc='left')
plt.legend().remove()
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
MAT_gb_graf = base64.b64encode(image_png)
MAT_gb_graf = MAT_gb_graf.decode('utf-8')





CD_gb_graf.plot(kind='barh',figsize=(15,12), color="blue")
plt.xlabel('Nivel de interesse')
plt.ylabel('Interesses')
plt.title('Visão geral dos interesses dos alunos de CD', loc='left')
plt.legend().remove()
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
CD_gb_graf = base64.b64encode(image_png)
CD_gb_graf = CD_gb_graf.decode('utf-8')




data_soma_interesse_graf.plot(kind='barh',figsize=(15,15), color="turquoise")
plt.xlabel('Nivel de interesse')
plt.ylabel('Interesses')
plt.title('Visão geral dos interesses', loc='left')
plt.legend().remove()
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
data_soma_interesse_graf = base64.b64encode(image_png)
data_soma_interesse_graf = data_soma_interesse_graf.decode('utf-8')


CD_MAT_graf[['grau_CD','grau_MAT']].plot(figsize=(15,12),kind='barh')
plt.xlabel('Nivel de interesse')
plt.ylabel('Interesses')
plt.title('Visão geral dos interesses dos alunos de CD', loc='left')
plt.legend()
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
CD_MAT_graf = base64.b64encode(image_png)
CD_MAT_graf = CD_MAT_graf.decode('utf-8')


def analise_daniel(request):
    context = {
        'alunos_head': alunos_head_html,
        'interesses_head': interesses_head_html, 
        'data' :data_html,
        'data_soma_interesse':data_soma_interesse_html,
        'data_soma_interesse_graf':data_soma_interesse_graf,

        'CD_gb':CD_gb_html,
        'CD_gb_graf':CD_gb_graf,

        'MAT_gb':MAT_gb_html,
        'MAT_gb_graf':MAT_gb_graf,

        'CD_MAT':CD_MAT_html,
        'CD_MAT_graf':CD_MAT_graf,
    }
    return render(request, 'daniel/main.html', context=context)
