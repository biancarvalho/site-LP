from django.shortcuts import render
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses

from io import BytesIO
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

alunos = Aluno.objects
interesses = Interesses.objects
alunos_interesses = Aluno_Interesses.objects

lista_alunos = alunos.values()
lista_interesses = interesses.values()
lista_alunos_interesses = alunos_interesses.values()

interesses_distintos = interesses.values('nome').distinct()

alunos_df = pd.DataFrame(lista_alunos)
interesses_df = pd.DataFrame(lista_interesses)

plt.plot(range(10))
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

graphic = base64.b64encode(image_png)
graphic = graphic.decode('utf-8')

def main(request):
    context = {
        'graphic': graphic,
        'df_alunos': alunos_df,
        'df_interesses': interesses_df,
        'interesses_distintos': interesses_distintos
    }
    return render(request, 'sylvio/main.html', context=context)
