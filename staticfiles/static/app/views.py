import json
import requests
from django.db.models import Q
from django.http import JsonResponse
from .models import Traduction,Contribution
from django.shortcuts import render, redirect
from django.contrib import messages


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
        ).values('francais')[:10]
        suggestions = [s['francais'] for s in suggestions_qs]
    return JsonResponse(suggestions, safe=False)




def traduction(request):
    phrase_francaise = request.POST.get('phrase_francaise', '').strip().capitalize()
    suggestions = []
    if phrase_francaise:
        # Utiliser la méthode "values" pour ne récupérer que la colonne "francais"
        suggestions_qs = Traduction.objects.filter(
            Q(francais__icontains=phrase_francaise) | Q(francais__istartswith=phrase_francaise)
        ).values('francais')[:10]
        suggestions = [s['francais'] for s in suggestions_qs]

    traduction_soninke = ''
    if phrase_francaise:
        if phrase_francaise in traductions:
            traduction_soninke = traductions[phrase_francaise]
        else:
            traduction_soninke = "Traduction indisponible pour l'instant"
    return render(request, 'index.html', {'traduction_soninke': traduction_soninke, 'suggestions': suggestions, 'phrase_francaise': phrase_francaise})

def traductionauto(request):
    url = "https://raw.githubusercontent.com/sibylassana95/Fran-ais-Soninke/main/data/langue.json"
    response = requests.get(url)
    data = json.loads(response.text)
    for traduction in data:
        francais = list(traduction.keys())[0]
        soninke = list(traduction.values())[0]
        francais = francais.capitalize()
        if not Traduction.objects.filter(francais=francais).exists():
            Traduction.objects.create(francais=francais, soninke=soninke)

    return render(request, 'index.html')



def contribution(request):
    if request.method == 'POST':
        nom_complet = request.POST.get('nom_complet')
        francais = request.POST.get('francais')
        soninke = request.POST.get('soninke')
        if len(nom_complet) > 30 or len(francais) > 30 or len(soninke) > 30:
            messages.error(request, 'Les mots ne doivent pas dépasser 30 caractères.')
        else:
            contribution = Contribution.objects.create(nom_complet=nom_complet, francais=francais, soninke=soninke)
            messages.success(request, 'Votre contribution a été ajoutée avec succès.')
            return redirect('contribution')
    return render(request, 'contribution.html')


def about(request):
    return render(request, 'about.html')

    
def error_404(request, exception):
    return render(request, 'page404.html')