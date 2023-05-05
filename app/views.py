import json
import requests
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import Traduction

# Charger les données de traduction en mémoire à l'initialisation de l'application
url = "https://raw.githubusercontent.com/sibylassana95/Fran-ais-Soninke/main/data/langue.json"
response = requests.get(url)
data = json.loads(response.text)
traductions = {}
for traduction in data:
    francais = list(traduction.keys())[0].capitalize()
    soninke = list(traduction.values())[0]
    traductions[francais] = soninke

def suggestions(request):
    phrase_francaise = request.GET.get('phrase', '')
    suggestions = []
    if phrase_francaise:
        # Utiliser la méthode "values" pour ne récupérer que la colonne "francais"
        suggestions_qs = Traduction.objects.filter(
            Q(francais__icontains=phrase_francaise) | Q(francais__istartswith=phrase_francaise)
        ).values('francais')[:5]
        suggestions = [s['francais'] for s in suggestions_qs]
    return JsonResponse(suggestions, safe=False)




def traduction(request):
    phrase_francaise = request.POST.get('phrase_francaise', '').strip().capitalize()
    suggestions = []
    if phrase_francaise:
        # Utiliser la méthode "values" pour ne récupérer que la colonne "francais"
        suggestions_qs = Traduction.objects.filter(
            Q(francais__icontains=phrase_francaise) | Q(francais__istartswith=phrase_francaise)
        ).values('francais')[:5]
        suggestions = [s['francais'] for s in suggestions_qs]

    traduction_soninke = ''
    if phrase_francaise:
        if phrase_francaise in traductions:
            traduction_soninke = traductions[phrase_francaise]
        else:
            traduction_soninke = "Traduction indisponible pour l'instant"
    return render(request, 'index.html', {'traduction_soninke': traduction_soninke, 'suggestions': suggestions, 'phrase_francaise': phrase_francaise})




def about(request):
    return render(request, 'about.html')
