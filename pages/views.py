from django.http.response import HttpResponseNotFound
from django.shortcuts import render

def perguntas(request, param):
    if param in range(1,8):
        return render(request, f'pages/pergunta{param}.html')
    else:
        return HttpResponseNotFound('Página não encontrada')    

def index(request):
    return render(request, 'pages/pagina_inicial.html')  

def cadastrar(request):
    return render(request, 'pages/cadastro.html')

def login(request):
    return render(request, 'pages/login.html')    

def recuperar_senha(request):
    return render(request, 'pages/recuperar_senha.html')    

def mudar_email(request):
    return render(request, 'pages/mudar_email.html')       
    
def mudar_senha(request):
    return render(request, 'pages/mudar_senha.html')    

def ranking(request):
    return render(request, 'pages/ranking.html')

def chat(request):
    return render(request, 'pages/chat.html')  
