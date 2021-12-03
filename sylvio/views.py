from django.shortcuts import render
import pandas as pd
from pages.models import Aluno, Interesses, Aluno_Interesses


def main(request):
    context = {
        
    }
    return render(request, 'sylvio/main.html', context=context)
