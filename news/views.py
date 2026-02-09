from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista   
import datetime
# Create your views here.

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti" : giornalisti}
    print(context)
    return render(request, "news/homepage.html", context)

def index(request):
    return render(request, "news/index.html")

def articoloDetailView(request, pk):
    articolo=get_object_or_404(Articolo, pk=pk)
    context={"articolo":articolo}
    return render(request, "lista_articoli.html", context)

def listaArticoli(request, pk=None):
    if(pk==None):
        articoli = Articolo.objects.all()
        giornalista=None
    else:
        articoli=Articolo.objects.filter(giornalista_id=pk)
        giornalista=Giornalista.objects.get(pk=pk)
    if(pk==None):
        is_giornalista=False
    else:
        is_giornalista=True
    context={
        'articoli':articoli,
        'is_giornalista':is_giornalista,
        'giornalista':giornalista
    }
    return render(request, 'lista_articoli.html', context)

def queryBase(request):
    #tutti gli articoli scritti da giornalisti di un certo cognome 
    articoli_cognome=Articolo.objects.filter(giornalista__cognome="Colombo")
    #totale 
    numero_totale_articoli = Articolo.objects.count()

    #contare numero articoli scritti da un giornalista specifico
    giornalista_1=Giornalista.objects.get(id=1)
    numero_articoli_giornalista_1=Articolo.objects.filter(giornalista=giornalista_1).count()

    #ordinare gli articoli per numero di visualizzazioni in ordine decrescente
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

    #tutti gli articoli che non hanno visualizzazioni
    articoli_senza_visualizzazioni=Articolo.objects.filter(visualizzazioni=0)

    #articolo più visualizzato
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()

    #tutti i giornalisti nati dopo una certa data
    giornalisti_data=Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990,1,1))

    #tutti gli articoli pubblicati in una data specifica
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023,1,1))

    #tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo=Articolo.objects.filter(data__range=(datetime.date(2023,1,1), datetime.date(2023,12,31)))

    #gli articoli scritti da giornalisti nati prima del 1980
    giornalisti_nati=Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980,1,1))
    articoli_giornalisti=Articolo.objects.filter(giornalista__in=giornalisti_nati)

    #il giornalista + giovane
    giornalista_giovane=Giornalista.objects.order_by('-anno_di_nascita').first()

    #il giornalista + vecchio
    giornalista_vecchio=Giornalista.objects.order_by('anno_di_nascita').first()

    #gli ultimi 5 articoli pubblicati
    ultimi=Articolo.objects.order_by('-data')[:5]

    #tutti gli articoli con un certo numero minimo di visualizzazioni
    articoli_minime_visualizzazioni=Articolo.objects.filter(visualizzazioni__gte=100)

    #tutti gli articoli che contengono una certa parola nel titolo
    articoli_parola=Articolo.objects.filter(titolo__icontains='articolo')

    #Articoli pubblicati in nun certo mese di un anno spcifico
    articoli_mese_anno=Articolo.objects.filter(data__month=1,data__year=2023)

    #Giornalisti con almeno un articolo con più di 100 visualizzazioni
    giornalisti_con_articoli_popolari=Giornalista.objects.filter(articoli__visualizzazioni__gt=100).distinct()

    data=datetime.date(1990,1,1)
    visualizzioni=50

    #scrivi quali articoli vengono selezionati
    articoli_con_and=Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzioni)

    #per mettere in or le condizioni utilizzare Q
    from django.db.models import Q
    #scrivi quali articoli vengono selezionati
    articoli_con_or=Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=data) | Q(visualizzazioni__lte=visualizzioni))

    #per il not utilizzare Q
    #scrivi quali articoli vengono selezionati
    articoli_con_not=Articolo.objects.filter(~Q(giornalista__anno_di_nascita__gt=data))
    #oppure con il metodo exclude
    articoli_con_not=Articolo.objects.exclude(giornalista__anno_di_nascita__lt=data)

    context={
        'articoli_cognome':articoli_cognome,
        'numero_totale_articoli':numero_totale_articoli,
        'numero_articoli_giornalista_1':numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni':articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato':articolo_piu_visualizzato,
        'giornalisti_data':giornalisti_data,
        'articoli_del_giorno':articoli_del_giorno,
        'articoli_periodo':articoli_periodo,
        'articoli_giornalisti':articoli_giornalisti,
        'giornalista_giovane':giornalista_giovane,
        'giornalista_vecchio':giornalista_vecchio,
        'ultimi':ultimi,
        'articoli_minime_visualizzazioni':articoli_minime_visualizzazioni,
        'articoli_parola':articoli_parola,
        'articoli_mese_anno':articoli_mese_anno,
        'giornalisti_con_articoli_popolari':giornalisti_con_articoli_popolari,
        'articoli_con_and':articoli_con_and,
        'articoli_con_or':articoli_con_or,
        'articoli_con_not':articoli_con_not,
    }

    return render(request, "query.html" ,context)

