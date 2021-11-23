from django.urls import path
from pages import views as views

urlpatterns=[
    path('pergunta1.html', views.perguntas, name='pergunta'), #Defini apenas uma pagina de pergunta definida aqui. Sugestão: realizar url dinâmica.
    path('pagina_inicial.html', views.index, name='pagina-inicial')
]