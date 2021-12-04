from django.urls import path
from raul import views as views

urlpatterns=[
    path('raul/main.html', views.analise_raul, name='analise_raul'),
]