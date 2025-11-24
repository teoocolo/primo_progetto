from django.urls import path
from prova_pratica_1.views import index, diff, pari

app_name="prova_pratica_1"
urlpatterns=[
    path('', index, name='index'),
    path('diff', diff, name='diff'),
    path('pari', pari, name='pari')
]