from django.urls import path
from sylvio import views as views

urlpatterns=[
    path('sylvio/main.html', views.main, name='main'),
]