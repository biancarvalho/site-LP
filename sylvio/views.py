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

df_faixas = df.copy(deep=True)
df_faixas["faixa_etaria"] = pd.cut(x=df_faixas['idade'], bins=[14,23,32,41,50], labels=["mais_jovens","jovens","velhos", "mais_velhos"])

df_mais_jovens = df_faixas[df_faixas["faixa_etaria"] == 'mais_jovens']
df_mais_jovens_frequencia = df_mais_jovens['nome_interesse'].value_counts().to_frame().reset_index()

df_mais_jovens_frequencia2 = df_mais_jovens_frequencia.iloc[::-1]
df_mais_jovens_sem_raros = df_mais_jovens.groupby('nome_interesse').filter(lambda x : len(x)>=5)
df_mais_jovens_frequencia3 = df_mais_jovens_sem_raros['nome_interesse'].value_counts(ascending=True).to_frame().reset_index()

df_mais_jovens_agrupado = df_mais_jovens_sem_raros.groupby(['nome_interesse'])
df_mais_jovens_grau = df_mais_jovens_agrupado.mean()['grau'].sort_values(ascending=False).to_frame()

df_mais_jovens_grau.plot(kind='barh',figsize=(13,8), color="turquoise")
plt.xlabel('Grau de interesse médio')
plt.ylabel('Interesses')
plt.title('Variação de interesses das idade de 15 a 23 anos', loc='left')
plt.legend().remove()


buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png1 = buffer.getvalue()
buffer.close()

graphic_mais_jovens = base64.b64encode(image_png1)
graphic_mais_jovens = graphic_mais_jovens.decode('utf-8')

# Preparando dataframes que serão mostrados.
alunos_head = html_updated = re.sub("class=\"dataframe ", "class=\"", alunos.head(5).to_html(classes='table table-striped', justify='left', index=False))
interesses_sample = html_updated = re.sub("class=\"dataframe ", "class=\"", interesses.sample(5).to_html(classes='table table-striped',justify='left', index=False))
alunos_interesses_head = html_updated = re.sub("class=\"dataframe ", "class=\"", alunos_interesses.head(5).to_html(classes='table table-striped',justify='left', index=False))

df = html_updated = re.sub("class=\"dataframe ", "class=\"", df.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_faixas = html_updated = re.sub("class=\"dataframe ", "class=\"", df_faixas.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_mais_jovens_frequencia = html_updated = re.sub("class=\"dataframe ", "class=\"", df_mais_jovens_frequencia.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_mais_jovens_frequencia2 = html_updated = re.sub("class=\"dataframe ", "class=\"", df_mais_jovens_frequencia2.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_mais_jovens_frequencia3 = html_updated = re.sub("class=\"dataframe ", "class=\"", df_mais_jovens_frequencia3.head(5).to_html(classes='table table-striped',justify='left', index=False))

df_mais_jovens_grau = html_updated = re.sub("class=\"dataframe ", "class=\"", df_mais_jovens_grau.head(5).to_html(classes='table table-striped',justify='left', index=True))






def main(request):
    context = {
        'alunos_head': alunos_head,
        'interesses_sample': interesses_sample,
        'alunos_interesses_head': alunos_interesses_head, 
        'merge_inicial': merge_inicial,
        'df': df,
        'df_faixas': df_faixas,
        'df_mais_jovens_frequencia': df_mais_jovens_frequencia,
        'df_mais_jovens_frequencia2': df_mais_jovens_frequencia2,
        'df_mais_jovens_frequencia3': df_mais_jovens_frequencia3,

        'df_mais_jovens_grau': df_mais_jovens_grau,
        'graphic_mais_jovens': graphic_mais_jovens,

    }
    return render(request, 'sylvio/main.html', context=context)
