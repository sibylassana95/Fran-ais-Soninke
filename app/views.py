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
    phrase = request.GET.get('phrase', '')
    direction = request.GET.get('direction', 'fr-sn')
    suggestions = []
    
    if phrase:
        if direction == 'fr-sn':
            suggestions_qs = Traduction.objects.filter(
                Q(francais__icontains=phrase) | Q(francais__istartswith=phrase)
            ).values('francais')[:10]
            suggestions = [s['francais'] for s in suggestions_qs]
        else:  # sn-fr
            suggestions_qs = Traduction.objects.filter(
                Q(soninke__icontains=phrase) | Q(soninke__istartswith=phrase)
            ).values('soninke')[:10]
            suggestions = [s['soninke'] for s in suggestions_qs]
    
    return JsonResponse(suggestions, safe=False)




def traduction(request):
    word_count = Traduction.objects.count()
    direction = request.POST.get('direction', 'fr-sn')  # fr-sn ou sn-fr
    
    if direction == 'fr-sn':
        phrase_input = request.POST.get('phrase_francaise', '').strip()
        phrase_clean = ' '.join(phrase_input.split()).capitalize()
        traduction_output = ''
        if phrase_clean:
            if phrase_clean in traductions:
                traduction_output = traductions[phrase_clean]
            else:
                traduction_output = "Traduction indisponible pour l'instant"
        return render(request, 'index.html', {
            'traduction_soninke': traduction_output,
            'phrase_francaise': phrase_input,
            'word_count': word_count,
            'direction': direction
        })
    else:  # sn-fr
        phrase_soninke = request.POST.get('phrase_soninke', '').strip()
        phrase_clean = ' '.join(phrase_soninke.split())
        traduction_francaise = ''
        if phrase_clean:
            for fr, sn in traductions.items():
                if sn.lower() == phrase_clean.lower():
                    traduction_francaise = fr
                    break
            if not traduction_francaise:
                traduction_francaise = "Traduction indisponible pour l'instant"
        return render(request, 'index.html', {
            'traduction_francaise': traduction_francaise,
            'phrase_soninke': phrase_soninke,
            'word_count': word_count,
            'direction': direction
        })

def traductionauto(request):
    url = "https://raw.githubusercontent.com/sibylassana95/Fran-ais-Soninke/main/data/langue.json"
    response = requests.get(url)
    data = json.loads(response.text)
    for traduction in data:
        francais = list(traduction.keys())[0].capitalize()
        soninke = list(traduction.values())[0]
        if not Traduction.objects.filter(francais=francais).exists():
            Traduction.objects.create(francais=francais, soninke=soninke)
    
    contributions = Contribution.objects.all()
    for contrib in contributions:
        francais = contrib.francais.strip().capitalize()
        soninke = contrib.soninke.strip()
        if not Traduction.objects.filter(francais=francais).exists():
            Traduction.objects.create(francais=francais, soninke=soninke)
    
    messages.success(request, 'Traductions ajoutées avec succès.')
    return redirect('traduction')



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

# Error handlers
def handler400(request, exception):
    return render(request, '400.html', status=400)

def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def handler503(request):
    return render(request, '503.html', status=503)
