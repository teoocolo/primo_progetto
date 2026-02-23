from django.urls import path 
from .views import home, articoloDetailView, index, listaArticoli, listaGiornalisti, giornalistaDetail, queryBase

app_name='news'

urlpatterns=[
    path('', home, name='homepage'),
    path('index', index, name='index'),
    path("articolo/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("lista_giornalisti", listaGiornalisti, name="lista_giornalisti"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("giornalista_detail/<int:pk>", giornalistaDetail, name="giornalista_detail"),
    path("query", queryBase, name="query"),
]   