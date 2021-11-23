from django.shortcuts import render

def ranking(request):
    return render(request, 'ranking.html')

def chat(request):
    return render(request, 'chat.html')  
