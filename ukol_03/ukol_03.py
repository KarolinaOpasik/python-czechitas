# Zadání

"""
Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

Soubor si ulož a načti do slovníku.

Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). 
Vytvoř nový slovník. Jeho klíče budou opět jména žáků, 
a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. 
Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.json.
"""

import json

with open("body.json", encoding="utf-8") as file:
    body = json.load(file)


prospech = {}


for keys, values in body.items():
    if values >= 60:                
        prospech[keys] = "Pass"
    else:                           
        prospech[keys] = "Fail"

with open("prospech.json", mode="w", encoding="utf-8") as file:
    json.dump(prospech, file, ensure_ascii=False, indent=4)


# Nepovinný bonus

"""
Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. 
Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.

Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. 
Bodová rozhraní (vztahují se na součet) najdeš zde:

1: 90 a více
2: 70-89
3: 50-69
4: 30-49
5: 29 a méně

Výsledný slovník ulož jako JSON do souboru znamky.json.
"""

with open("bonusy.json", encoding="utf-8") as file:
    bonusy = json.load(file)

for keys in bonusy:
    body[keys] += bonusy[keys]

znamky = {}

for keys in body:
    if body[keys] >= 90:
        znamky[keys] = 1
    elif 89 > body[keys] >= 70:
        znamky[keys] = 2  
    elif 69 > body[keys] >= 50:
        znamky[keys] = 3
    elif 49 > body[keys] >= 30:
        znamky[keys] = 4
    else:
        znamky[keys] = 5

with open("znamky.json", mode="w", encoding="utf-8") as file:
    json.dump(znamky, file, ensure_ascii=False, indent=4)
