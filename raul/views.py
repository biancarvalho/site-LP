from django.shortcuts import render
import pandas as pd
from pages.models import *
import re
from io import BytesIO
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sylvio import views as base_analise

df2 = base_analise.df.groupby('id_aluno')

new_df = base_analise.df.merge(base_analise.df, on='id_aluno')

df0 = (new_df[new_df['nome_interesse_x'].lt(new_df['nome_interesse_y'])]
    .groupby(['id_aluno', 'nome_interesse_x', 'nome_interesse_y']) 
    .size().sum(level=[1,2]).to_frame().sort_values(by=0, ascending=False)
)
df1 = (new_df[new_df['nome_interesse_x'].lt(new_df['nome_interesse_y'])]
    .groupby(['id_aluno', 'nome_interesse_x', 'nome_interesse_y'])["grau_x", "grau_y"]
    .apply(lambda x : x.astype(int).sum())
)

df2 = df1[['grau_x', 'grau_y']].sum(level=[1, 2])
df2['soma'] = df2['grau_x'] + df2['grau_y']
df2 = df2.sort_values(by='soma', ascending=False)


df3 = df1[['grau_x', 'grau_y']].mean(level=[1, 2])%5
df3['media'] = df3['grau_x'] + df3['grau_y']
df3 = df3.sort_values(by='media', ascending=False)

df0 = html_updated = re.sub("class=\"dataframe ", "class=\"", df0.head(20).to_html(classes='table table-striped',justify='left', index=True))

df2 = html_updated = re.sub("class=\"dataframe ", "class=\"", df2.head(20).to_html(classes='table table-striped',justify='left', index=True))

df3 = html_updated = re.sub("class=\"dataframe ", "class=\"", df3.head(20).to_html(classes='table table-striped',justify='left', index=True))


def main(request):
    context = {
        'df': base_analise.df_head,
        'df0': df0,
        'df2': df2,
        'df3': df3,
    }
    return render(request, 'raul/main.html', context=context)
