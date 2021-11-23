from django.shortcuts import render

def perguntas(request):
    return render(request, 'pergunta1.html')

def index(request):
    return render(request, 'pagina_inicial.html')  
