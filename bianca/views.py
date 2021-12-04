from django.shortcuts import render
import pandas as pd
from pages.models import *
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

df = merge_inicial[['id_aluno_interesse','id_aluno','id_interesse','nome_aluno','sexo','idade','categoria','nome_interesse','grau']]

# Filtrando os dados para grande grau de interesse, ou seja, maior ou igual a 3 e separando por sexo.
df_m = df[(df.sexo == 'M') & (df.grau >= 3)]
df_f = df[(df.sexo == 'F') & (df.grau >= 3)]
freq = df.groupby(['categoria']).count()
df['sexo'].replace(to_replace='F', value=1, inplace=True)
df['sexo'].replace(to_replace='M', value=0, inplace=True)
df1 = df.groupby(['categoria'])

df1.plot(x="categoria", y="sexo", kind="bar") 
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

graphic = base64.b64encode(image_png)
graphic = graphic.decode('utf-8')

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
        'graphic': graphic,
    }
    return render(request, 'bianca/analises.html', context=context)
