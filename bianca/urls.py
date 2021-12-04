from django.urls import path
from bianca import views as views

urlpatterns=[
    path('bianca/analises.html', views.analises_bianca, name='analises_bianca')
]