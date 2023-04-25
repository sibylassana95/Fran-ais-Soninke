import json

import requests
from django.db.models import Q
from django.shortcuts import render

from .models import Traduction


def traduction(request):
    url = "https://raw.githubusercontent.com/sibylassana95/Fran-ais-Soninke/main/data/langue.json"
    response = requests.get(url)
    data = json.loads(response.text)
    for traduction in data:
        francais = list(traduction.keys())[0]
        soninke = list(traduction.values())[0]
        francais = francais.capitalize()
        if not Traduction.objects.filter(francais=francais).exists():
            Traduction.objects.create(francais=francais, soninke=soninke)
    if request.method == 'POST':
        phrase_francaise = request.POST.get('phrase_francaise')
        phrase_francaise = phrase_francaise.strip()
        phrase_francaise = phrase_francaise.capitalize()
        try:
            traduction_soninke = Traduction.objects.get(francais=phrase_francaise).soninke
        except Traduction.DoesNotExist:
            traduction_soninke = "Traduction indisponible pour l'instant"
        return render(request, 'index.html', {'traduction_soninke': traduction_soninke})
    else:
        return render(request, 'index.html')


def about(resquest):
    return render(resquest, 'about.html')