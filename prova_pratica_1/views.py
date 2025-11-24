from django.shortcuts import render
import random
def index(request):
    return render(request, "prova_pratica_1/index.html")

def diff(request):
    context={
        'var1':random.randint(1,20),
        'var2':random.randint(1,20),
    }
    return render(request, "prova_pratica_1/diff.html", context)

def pari(request):
    numeri=[]
    contatore_pari=0
    contatore_dispari=0
    for i in range(15):
        n=random.randint(1,20)
        if(n%2==0):
            contatore_pari+=1
        else:
            contatore_dispari+=1
        numeri.append(n)
    context={
        'numeri':numeri,
        'contatore_pari':contatore_pari,
        'contatore_dispari':contatore_dispari,
    }
    return render(request, "prova_pratica_1/pari.html", context)
    return render(request, "prova_pratica_1/pari.html", context)

