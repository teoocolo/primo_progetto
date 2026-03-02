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
        "elenco_materie": materie,
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
    for studente, valutazioni in voti.items():
        max=0
        min=0
        materia_max=""
        materia_min=""
        studente_max=""
        studente_min=""
        for materia, voto, peso in valutazioni:
            if voto > max:
                max = voto
            if voto < min:
                min = voto
        context={
            "max": max,
            "min": min,
            "studente_max": studente_max,
            "studente_min": studente_min,
            "materia_max": materia_max,
            "materia_min": materia_min
        }
    return render(request, "voti/max_min.html", context)

