import json

with open('data/contribution.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    item['nom_complet'] = item['nom_complet'].strip()
    item['francais'] = item['francais'].strip()
    item['soninke'] = item['soninke'].strip()

with open('data/contribution.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Fichier nettoyé!")
