from django.urls import path
from pages import views as views

urlpatterns=[
    path('pergunta<int:param>', views.perguntas, name='pergunta'),
    path('pagina_inicial.html', views.index, name='pagina-inicial'),
    path('', views.login, name='index'),
    path('login.html', views.login, name='login'),
    path('cadastro.html', views.cadastrar, name='cadastro'),
    path('recuperar_senha.html', views.recuperar_senha, name='recuperar-senha'),
    path('mudar_email.html', views.mudar_email, name='mudar-email'),
    path('mudar_senha.html', views.mudar_senha, name='mudar-senha'),
    path('ranking.html', views.rankings, name='ranking'),
    path('chat.html', views.chat, name='chat')
]