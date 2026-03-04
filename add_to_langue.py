import json

# Charger contribution.json
with open('data/contribution.json', 'r', encoding='utf-8') as f:
    contributions = json.load(f)

# Charger langue.json
with open('data/langue.json', 'r', encoding='utf-8') as f:
    langue = json.load(f)

# Ajouter les contributions au format {francais: soninke}
for item in contributions:
    francais = item['francais'].strip()
    soninke = item['soninke'].strip()
    langue.append({francais: soninke})

# Sauvegarder langue.json
with open('data/langue.json', 'w', encoding='utf-8') as f:
    json.dump(langue, f, ensure_ascii=False, indent=2)

print(f"Ajouté {len(contributions)} contributions à langue.json")
