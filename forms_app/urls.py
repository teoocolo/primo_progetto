from django.urls import path
from .views import contatti, lista_contatti, modifica_contatto, elimina_contatto, index
app_name = "forms_app"

urlpatterns = [
    path('', index, name='index'),
    path('contattaci', contatti, name='contatti'),
    path('lista_contatti', lista_contatti, name='lista_contatti'),
    path('modifica_contatto/<int:pk>', modifica_contatto, name='modifica_contatto'),
    path('elimina_contatto/<int:pk>', elimina_contatto, name='elimina_contatto'),  
]