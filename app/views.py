import json

import requests
from django.shortcuts import render

from .models import Traduction

url = "https://raw.githubusercontent.com/bambadiagne/github-user-stats/master/users.json"
response = requests.get(url)
data = json.loads(response.text)

for traduction in data:
    francais = list(traduction.keys())[0]
    soninke = list(traduction.values())[0]
    Traduction.objects.create(francais=francais, soninke=soninke)


def traduction(request):
    if request.method == 'POST':
        phrase_francaise = request.POST.get('phrase_francaise')
        try:
            traduction_soninke = Traduction.objects.get(francais=phrase_francaise).soninke
        except Traduction.DoesNotExist:
            traduction_soninke = 'Traduction indisponible'
        return render(request, 'traduction.html', {'traduction_soninke': traduction_soninke})
    else:
        return render(request, 'traduction.html')
