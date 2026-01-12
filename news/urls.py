from django.urls import path 
from .views import home, articoloDetailView, index

app_name='news'

urlpatterns=[
    path('', home, name='homeview'),
    path('index', index, name='index'),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
]   