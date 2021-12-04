from django.shortcuts import render
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses
import re



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



# Preparando dataframes que serão mostrados.
alunos_head = html_updated = re.sub("class=\"dataframe ", "class=\"", alunos.head(5).to_html(classes='table table-striped',justify='left'))
interesses_head = html_updated = re.sub("class=\"dataframe ", "class=\"", interesses.head(5).to_html(classes='table table-striped',justify='left'))
merge_limpo = html_updated = re.sub("class=\"dataframe ", "class=\"", merge_limpo.head(5).to_html(classes='table table-striped',justify='left'))
merge_inicial = html_updated = re.sub("class=\"dataframe ", "class=\"", merge_inicial.head(5).to_html(classes='table table-striped',justify='left'))


def analise_raul(request):

    context = {
        'alunos_head': alunos_head,
        'interesses_head': interesses_head, 
        'merge_inicial' :merge_inicial,
        'merge_limpo':merge_limpo,
        
    }
    return render(request, 'raul/analise_raul.html', context=context)
