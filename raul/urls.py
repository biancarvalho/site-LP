from django.urls import path
from raul import views as views

urlpatterns=[
    path('raul/analise_raul.html', views.analise_raul, name='analise_raul'),
]