# Zadani

"""
Vyvíjíš software pro obchod s elektronickými součástkami. 
Firma eviduje informace o počtu součástek na skladě ve slovníku. 
Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. 
Software se nejprve zeptá na kód součástky a poté na množství, 
které si zákazník chce koupit. Obě informace si ulož. 

Následně naprogramuj následující varianty:

Pokud zadaný kód není ve slovníku, není součástka skladem. 
Vypiš tedy zprávu, že součástka není skladem.

Pokud zadaná součástka na skladě je, ale je jí méně, 
než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. 
Následně součástku odeber ze slovníku, protože je vyprodaná.

Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, 
že poptávku lze uspokojit v plné výši, a sniž počet součástek
na skladě o množství požadované zákazníkem.
"""

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_produktu = input("Zadej kód součástky: ")

if kod_produktu not in sklad:
    print("Součástka není skladem.")
else:
    mnozstvi = int(input("Zadej množství: "))
    if mnozstvi > sklad[kod_produktu]:
        print(f"Lze prodat pouze {sklad[kod_produktu]} kusů.")
        sklad.pop(kod_produktu)
    else:
        print("Poptávku lze uspokojit v plné výši.")
        sklad[kod_produktu] -= mnozstvi



# Bonus 1

"""
Ve slovníku najdeš Morseovu abecedu, kde jako klíč slouží znak v 
klasické abecedě a jako hodnota zápis znaku v Morseově abecedě.

1. Napiš program, který se uživatele zeptá na text, který chce zapsat v Morseově abecedě. 
Uvažuj disciplinovaného uživatele, který zadává pouze znaky bez diakritiky, 
malá písmena atd. Na začátku uvažuj i to, že uživatel nezadává mezery.

2. Projdi řetězec zadaný uživatelem. Najdi každý znak ve slovníku
a vypiš ho na obrazovku v Morseově abecedě.

3. Abychom měli celý kód vypsaný na jedné řádce, požádáme funkci print(), 
aby na konci výpisu nevkládala znak pro konec řádku, ale mezeru. 
To uděláme tak, že jako druhý argument funkce dáme argument end=" ".

4. Nyní přidáme mezery. Uvažuj, že uživatel může zadat mezeru. 
Před tím, než budeš hledat znak ve slovníku, zkontroluj, zda znak není mezera. 
Pokud ano, vypiš znak lomítka /.
"""


morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

text = input("Zadej text, který chceš zapsat v Morseově abecedě: ")

if " " in text:
    new_text = text.replace(" ", "/")
else:
    new_text = text

for i in new_text:
    print(morse_code[i], end=" ")



# Bonus 2

"""
Ve slovníku zde najdeš seznam slovníků s informacemi o státech světa. 
O každém státu tam vidíš následující informace:

název státu (name),
hlavní město (capital),
region (region),
subregion (subregion),
populace (population),
rozloha (area),
Giniho koeficient (gini).

Vytvoř program, který se uživatele zeptá na region, který ho zajímá. 
Následně projdi seznam a vypiš všechny státy, které leží v regionu. 
Pokud program žádný stát pro daný region nenajde, vypiš text "Neznámý region".
"""


staty = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "region": "Asia",
        "subregion": "Southern Asia",
        "population": 27657145,
        "area": 652230.0,
        "gini": 27.8,
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "region": "Europe",
        "subregion": "Northern Europe",
        "population": 28875,
        "area": 1580.0,
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "region": "Europe",
        "subregion": "Southern Europe",
        "population": 2886026,
        "area": 28748.0,
        "gini": 34.5,
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "region": "Africa",
        "subregion": "Northern Africa",
        "population": 40400000,
        "area": 2381741.0,
        "gini": 35.3,
    },
]

# Nebyla jsem si jista, jak ma vypadat vystup,
# proto jsem udelala dve reseni.
# Bohuzel me nenapadlo, jak bez pouziti seznamu "regions"
# dostat vystup jako u druheho reseni.

region_name = input("Zadej region, který tě zajímá: ").title()

# 1
regions = []

for item in staty:
    if item not in regions:
        regions.append(item["region"])

if region_name in regions:
    print(f"V regionu {region_name} se nachází následující státy: ")
    for item in staty:
        if region_name == item["region"]:
            print(item["name"])
else:
    print("Neznámý region")

# 2
print(f"V regionu {region_name} se nachází následující státy: ")
for item in staty:
    if region_name == item["region"]:
        print(item["name"])
    else:
        print("Neznámý region")
