from django.urls import path
from chats import views as views

urlpatterns=[
    path('ranking.html', views.ranking, name='ranking'),
    path('chat.html', views.chat, name='chat')
]