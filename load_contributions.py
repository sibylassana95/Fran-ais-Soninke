import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Soninke.settings')
django.setup()

from app.models import Traduction

with open('data/contribution.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    francais = item['francais'].strip().capitalize()
    soninke = item['soninke'].strip()
    if not Traduction.objects.filter(francais=francais).exists():
        Traduction.objects.create(francais=francais, soninke=soninke)
        print(f"Ajouté: {francais} -> {soninke}")

print(f"\nTotal: {Traduction.objects.count()} traductions")
