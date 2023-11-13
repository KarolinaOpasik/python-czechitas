class Auta:
    """Class representing a car."""

    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupnost=True,):
        """Initialize attributes to describe a car."""
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = dostupnost

    def pujc_auto(self):
        """Check if the car is available and return a hire confirmation or 
        statement showing that the car is not available."""
        if self.dostupnost is True:
            self.dostupnost = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."

    def get_info(self):
        """Return formatted information about a car."""
        return f"Značka a typ: {self.typ_vozidla}, registrační značka: {self.registracni_znacka}."

    def vrat_auto(self, stav_tachometru_pri_vraceni: int, pocet_dni: int):
        """Update car's availability and mileage and 
        calculate and return price for hiring the car."""
        self.najete_km = stav_tachometru_pri_vraceni
        self.dostupnost = True
        cena_den = 400 if pocet_dni < 7 else 300
        cena_pujceni = cena_den * pocet_dni
        return f"Cena za vypůjčení auta je {cena_pujceni}."


auto1 = Auta("4A2 302", "Peugeot 403 Cabrio", 47534)
auto2 = Auta("1P3 474", "Škoda Octavia", 41253)

znacka = input("Jakou značku si přejes půjčit? ").strip().title()
if znacka == "Peugeot":
    znacka = auto1
    print(auto1.get_info())
elif znacka == "Škoda":
    znacka = auto2
    print(auto2.get_info())
else:
    print("Bohužel tuto značku nemáme k dispozici.")

print(znacka.pujc_auto())

stav_tachometru = int(input("Zadej aktualní stav tachometru: "))
pocet_dni = int(input("Kolik dní bylo auto půjčené? "))
print(znacka.vrat_auto(stav_tachometru, pocet_dni))