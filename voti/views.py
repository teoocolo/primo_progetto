from django.shortcuts import render

# Create your views here.

materie=["Matematica","Italiano","Inglese","Storia","Geografia"]
voti= {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

def index(request):
    return render(request, "voti/index.html")
    
def view_a(request):
    context={
        "materie": materie,
    }
    return render(request, "voti/materie.html", context)    

def view_b(request):
    context = {
        "voti": voti,
    }
    return render(request, "voti/voti.html", context)
    
def view_c(request):
    print("Media voti per studente:")
    medie = {}
    for studente in voti:
        media = 0
        for voto in voti[studente]:
            media += voto[1]
        if len(voti[studente]) > 0:
            media = media / len(voti[studente])
            medie[studente] = media
        else:
            print("Non ci sono voti per lo studente", studente)
            medie[studente] = 0
        print(f"{studente} ha una media di {media}")
    context = {
        "media": medie
    }
    return render(request, "voti/media.html", context)

def view_d(request):
    # 1. Troviamo i valori numerici min e max assoluti
    tutti_i_voti = []
    for lista in voti.values():
        for item in lista:
            tutti_i_voti.append(item[1]) # item[1] è il voto
            
    val_max = max(tutti_i_voti)
    val_min = min(tutti_i_voti)

    # 2. Troviamo CHI ha preso quei voti e in QUALI materie
    # Usiamo set() per evitare duplicati, poi convertiamo in list()
    studenti_max = set()
    materie_max = set()
    studenti_min = set()
    materie_min = set()

    for studente, lista_voti in voti.items():
        for materia, voto, assenze in lista_voti:
            if voto == val_max:
                studenti_max.add(studente)
                materie_max.add(materia)
            if voto == val_min:
                studenti_min.add(studente)
                materie_min.add(materia)

    context = {
        'v_max': val_max,
        'stud_max': list(studenti_max),
        'mat_max': list(materie_max),
        'v_min': val_min,
        'stud_min': list(studenti_min),
        'mat_min': list(materie_min),
    }
    return render(request, "voti/max_min.html", context)