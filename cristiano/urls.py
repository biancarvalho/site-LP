from django.urls import path
from cristiano import views as views

urlpatterns=[
    path('cristiano/main.html', views.eda, name='eda'),
]