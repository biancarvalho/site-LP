from django.contrib import admin
from django.urls import path
from pages import views as views

urlpatterns=[
    path('bianca/analises.html', views.analises_bianca, name='analises_bianca')
]