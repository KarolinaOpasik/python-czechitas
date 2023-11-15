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


# create objects
auto1 = Auta("4A2 302", "Peugeot 403 Cabrio", 47534)
auto2 = Auta("1P3 474", "Škoda Octavia", 41253)

# ask user for the car they want to hire
znacka = input("Jakou značku si přejes půjčit? ").strip().title()
# print information about the car, rent it if available and calculate price for hiring
if znacka == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
    stav_tachometru = int(input("Zadej stav tachometru při vrácení: "))
    pocet_dni = int(input("Kolik dní bylo auto půjčené? "))
    print(auto1.vrat_auto(stav_tachometru, pocet_dni))
elif znacka == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
    stav_tachometru = int(input("Zadej stav tachometru při vrácení: "))
    pocet_dni = int(input("Kolik dní bylo auto půjčené? "))
    print(auto2.vrat_auto(stav_tachometru, pocet_dni))
else:
    print("Bohužel tuto značku nemáme k dispozici.")
