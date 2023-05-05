import json
import requests
from django.db.models import Q
from django.shortcuts import render
from .models import Traduction

from django.http import JsonResponse

def suggestions(request):
    phrase_francaise = request.GET.get('phrase', '')
    suggestions = []
    if phrase_francaise:
        suggestions = Traduction.objects.filter(Q(francais__icontains=phrase_francaise) | Q(francais__istartswith=phrase_francaise)).values_list('francais', flat=True)[:10]
    return JsonResponse(list(suggestions), safe=False)


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

    phrase_francaise = request.POST.get('phrase_francaise', '').strip().capitalize()
    suggestions = []
    if phrase_francaise:
        suggestions = Traduction.objects.filter(Q(francais__icontains=phrase_francaise) | Q(francais__istartswith=phrase_francaise)).values_list('francais', flat=True)[:5]

    traduction_soninke = ''
    if request.method == 'POST':
        try:
            traduction_soninke = Traduction.objects.get(francais=phrase_francaise).soninke
        except Traduction.DoesNotExist:
            traduction_soninke = "Traduction indisponible pour l'instant"
    return render(request, 'index.html', {'traduction_soninke': traduction_soninke, 'suggestions': suggestions, 'phrase_francaise': phrase_francaise})


def about(request):
    return render(request, 'about.html')
