from django.urls import path
from raul import views as views

urlpatterns=[
    path('raul/main.html', views.main, name='analise_raul'),
]