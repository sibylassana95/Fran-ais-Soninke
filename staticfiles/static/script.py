import json

import requests

from app.models import Traduction

url = "https://raw.githubusercontent.com/sibylassana95/Fran-ais-Soninke/main/data/langue.json"
response = requests.get(url)
data = json.loads(response.text)

for traduction in data:
    francais = list(traduction.keys())[0]
    soninke = list(traduction.values())[0]
    if not Traduction.objects.filter(francais=francais).exists():
        Traduction.objects.create(francais=francais, soninke=soninke)
