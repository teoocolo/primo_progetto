from django.urls import path 
from .views import home, articoloDetailView, index, listaArticoli, queryBase

app_name='news'

urlpatterns=[
    path('', home, name='homeview'),
    path('index', index, name='index'),
    path("articolo/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("query", queryBase, name="query"),



]   