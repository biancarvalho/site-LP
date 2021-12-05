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


matplotlib.rcParams.update({'font.size': 12,
                            'font.family': 'sans-serif'})

df_mais_jovens_grau.iloc[::-1].plot(kind='barh',figsize=(9,12), color="turquoise", )
plt.xlabel('Grau de interesse médio')
plt.ylabel('Interesses')
plt.title('Média do grau por interesse entre mais jovens (15 a 23 anos)', loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png', bbox_inches='tight')
buffer.seek(0)
image_png1 = buffer.getvalue()
buffer.close()

graphic_mais_jovens = base64.b64encode(image_png1)
graphic_mais_jovens = graphic_mais_jovens.decode('utf-8')

df_jovens = df_faixas[df_faixas["faixa_etaria"] == 'jovens']
df_jovens_frequencia = df_jovens['nome_interesse'].value_counts().to_frame().reset_index()

df_jovens_frequencia2 = df_jovens_frequencia.iloc[::-1]
df_jovens_sem_raros = df_jovens.groupby('nome_interesse').filter(lambda x : len(x)>=5)

df_jovens_agrupado = df_jovens_sem_raros.groupby(['nome_interesse'])
df_jovens_grau = df_jovens_agrupado.mean()['grau'].sort_values(ascending=False).to_frame()

df_jovens_grau.iloc[::-1].plot(kind='barh',figsize=(9,12), color="red", )
plt.xlabel('Grau de interesse médio')
plt.ylabel('Interesses')
plt.title('Média do grau por interesse entre jovens (24 a 32 anos)', loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png', bbox_inches='tight')
buffer.seek(0)
image_png2 = buffer.getvalue()
buffer.close()

graphic_jovens = base64.b64encode(image_png2)
graphic_jovens = graphic_jovens.decode('utf-8')

df_velhos = df_faixas[df_faixas["faixa_etaria"] == 'velhos']
df_velhos_frequencia = df_velhos['nome_interesse'].value_counts().to_frame().reset_index()

df_velhos_frequencia2 = df_velhos_frequencia.iloc[::-1]
df_velhos_sem_raros = df_velhos.groupby('nome_interesse').filter(lambda x : len(x)>=5)

df_velhos_agrupado = df_velhos_sem_raros.groupby(['nome_interesse'])
df_velhos_grau = df_velhos_agrupado.mean()['grau'].sort_values(ascending=False).to_frame()

df_velhos_grau.iloc[::-1].plot(kind='barh',figsize=(9,12), color="green", )
plt.xlabel('Grau de interesse médio')
plt.ylabel('Interesses')
plt.title('Média do grau por interesse entre velhos (33 a 41 anos)', loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png', bbox_inches='tight')
buffer.seek(0)
image_png3 = buffer.getvalue()
buffer.close()

graphic_velhos = base64.b64encode(image_png3)
graphic_velhos = graphic_velhos.decode('utf-8')

df_mais_velhos = df_faixas[df_faixas["faixa_etaria"] == 'mais_velhos']
df_mais_velhos_frequencia = df_mais_velhos['nome_interesse'].value_counts().to_frame().reset_index()

df_mais_velhos_frequencia2 = df_mais_velhos_frequencia.iloc[::-1]
df_mais_velhos_sem_raros = df_mais_velhos.groupby('nome_interesse').filter(lambda x : len(x)>=5)

df_mais_velhos_agrupado = df_mais_velhos_sem_raros.groupby(['nome_interesse'])
df_mais_velhos_grau = df_mais_velhos_agrupado.mean()['grau'].sort_values(ascending=False).to_frame()

df_mais_velhos_grau.iloc[::-1].plot(kind='barh',figsize=(9,12), color="purple", )
plt.xlabel('Grau de interesse médio')
plt.ylabel('Interesses')
plt.title('Média do grau por interesse entre mais velhos (42 a 50 anos)', loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png', bbox_inches='tight')
buffer.seek(0)
image_png4 = buffer.getvalue()
buffer.close()

graphic_mais_velhos = base64.b64encode(image_png4)
graphic_mais_velhos = graphic_mais_velhos.decode('utf-8')


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

df_jovens_frequencia = html_updated = re.sub("class=\"dataframe ", "class=\"", df_jovens_frequencia.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_jovens_frequencia2 = html_updated = re.sub("class=\"dataframe ", "class=\"", df_jovens_frequencia2.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_jovens_grau = html_updated = re.sub("class=\"dataframe ", "class=\"", df_jovens_grau.head(5).to_html(classes='table table-striped',justify='left', index=True))

df_velhos_frequencia = html_updated = re.sub("class=\"dataframe ", "class=\"", df_velhos_frequencia.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_velhos_frequencia2 = html_updated = re.sub("class=\"dataframe ", "class=\"", df_velhos_frequencia2.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_velhos_grau = html_updated = re.sub("class=\"dataframe ", "class=\"", df_velhos_grau.head(5).to_html(classes='table table-striped',justify='left', index=True))

df_mais_velhos_frequencia = html_updated = re.sub("class=\"dataframe ", "class=\"", df_mais_velhos_frequencia.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_mais_velhos_frequencia2 = html_updated = re.sub("class=\"dataframe ", "class=\"", df_mais_velhos_frequencia2.head(5).to_html(classes='table table-striped',justify='left', index=False))
df_mais_velhos_grau = html_updated = re.sub("class=\"dataframe ", "class=\"", df_mais_velhos_grau.head(5).to_html(classes='table table-striped',justify='left', index=True))



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

        'df_jovens_frequencia': df_jovens_frequencia,
        'df_jovens_frequencia2': df_jovens_frequencia2,
        'df_jovens_grau': df_jovens_grau,
        'graphic_jovens': graphic_jovens,

        'df_velhos_frequencia': df_velhos_frequencia,
        'df_velhos_frequencia2': df_velhos_frequencia2,
        'df_velhos_grau': df_velhos_grau,
        'graphic_velhos': graphic_velhos,

        'df_mais_velhos_frequencia': df_mais_velhos_frequencia,
        'df_mais_velhos_frequencia2': df_mais_velhos_frequencia2,
        'df_mais_velhos_grau': df_mais_velhos_grau,
        'graphic_mais_velhos': graphic_mais_velhos,

    }
    return render(request, 'sylvio/main.html', context=context)
