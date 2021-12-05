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
from sylvio import views as base_analise

# Filtrando os dados
df_sexo = base_analise.df[['sexo','grau','nome_interesse','categoria']]

##Separando a tabela pelo sexo
#Tabela de interesses de pessoas do sexo feminino  
df_f = df_sexo[df_sexo['sexo']=='F']

#Tabela de interesses de pessoas do sexo mascFalulino  
df_m = df_sexo[df_sexo['sexo']=='M']


## Graficos 


plt.clf()
plt.figure(figsize=(9, 12))
sns.violinplot(data=base_analise.df, x="grau", y="categoria", hue="sexo",
               split=True, inner="quart", linewidth=1, palette='bright')

plt.xlabel('Grau de interesse',          
           fontdict={
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.ylabel('Interesses',          
           fontdict={
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.title('Variação do grau de interesses por gênero', 
          fontdict={
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 20},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png', bbox_inches='tight')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

grafico1 = base64.b64encode(image_png)
grafico1 = grafico1.decode('utf-8')

#grafico sexo masculino
plt.rcParams.update({'font.size': 12,
                            'font.family': 'sans-serif'})
plt.figure(figsize=(8, 12))                    
sns.boxplot(x='grau', y='nome_interesse', data=df_m)

plt.xlabel('Grau de interesse',          
           fontdict={
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.ylabel('Interesses',          
           fontdict={'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.title('Variação de interesses do sexo masculino', 
          fontdict={'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 20},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png', bbox_inches='tight')
buffer.seek(0)
image_png2 = buffer.getvalue()
buffer.close()

grafico2 = base64.b64encode(image_png2)
grafico2 = grafico2.decode('utf-8')

#grafico sexo feminino

plt.figure(figsize=(9,12))                    
sns.boxplot(x='grau', y='nome_interesse', data=df_f)

plt.xlabel('Grau de interesse',          
           fontdict={
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.ylabel('Interesses',          
           fontdict={
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10})

plt.title('Variação de interesses do sexo feminino', 
          fontdict={
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 20},
          loc='left')
plt.legend().remove()

buffer = BytesIO()
plt.savefig(buffer, format='png', bbox_inches='tight')
buffer.seek(0)
image_png3 = buffer.getvalue()
buffer.close()

grafico3 = base64.b64encode(image_png3)
grafico3 = grafico3.decode('utf-8')


# Preparando dataframes que serão mostrados.
df_m = html_updated = re.sub("class=\"dataframe ", "class=\"", df_m.sample(5).to_html(classes='table table-striped',justify='left'))
df_f = html_updated = re.sub("class=\"dataframe ", "class=\"", df_f.sample(5).to_html(classes='table table-striped',justify='left'))


def analises_bianca(request):
    context = {
        'df': base_analise.df_head,
        'df_f': df_f,
        'df_m': df_m,
        'grafico1': grafico1,
        'grafico2': grafico2,
        'grafico3': grafico3,
    }
    return render(request, 'bianca/main.html', context=context)