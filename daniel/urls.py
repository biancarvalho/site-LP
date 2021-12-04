from django.urls import path
from daniel import views as views

urlpatterns=[
    path('daniel/main.html', views.eda, name='eda'),
]