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

merge_limpo_html = html_updated = re.sub("class=\"dataframe ", "class=\"", merge_limpo.head(5).to_html(classes='table table-striped',justify='left'))
merge_inicial_html = html_updated = re.sub("class=\"dataframe ", "class=\"", merge_inicial.head(5).to_html(classes='table table-striped',justify='left'))


plt.clf()
plt.plot(range(10))

buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png_1 = buffer.getvalue()
buffer.close()

graphic_1 = base64.b64encode(image_png_1)
graphic_1 = graphic_1.decode('utf-8')

def main(request):
    context = {
        'graphic_1': graphic_1,
        'merge_inicial' :merge_inicial_html,
        'merge_limpo':merge_limpo_html,
    }
    return render(request, 'sylvio/main.html', context=context)
