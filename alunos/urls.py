from django.urls import path
from alunos import views as views

urlpatterns=[
    path('', views.login, name='index'),
    path('login.html', views.login, name='login'),
    path('cadastro.html', views.cadastrar, name='cadastro'),
    path('recuperar_senha.html', views.recuperar_senha, name='recuperar-senha'),
    path('mudar_email.html', views.mudar_email, name='mudar-email'),
    path('mudar_senha.html', views.mudar_senha, name='mudar-senha'),
]