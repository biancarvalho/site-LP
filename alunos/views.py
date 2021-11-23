from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')    

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')    

def mudar_email(request):
    return render(request, 'mudar_email.html')       
    
def mudar_senha(request):
    return render(request, 'mudar_senha.html')     