from django.urls import path
from cristiano import views as views

urlpatterns=[
    path('cristiano/eda.html', views.eda, name='eda'),
]