# ZADANI

jmeno = "Karolina"
emailova_adresa = jmeno + "@czechitas.cz"

print(emailova_adresa)


# BONUS

jmeno_a_prijmeni = input("Zadej své jméno a příjmení: ").split(" ")
jmeno = jmeno_a_prijmeni[0]
prijmeni = jmeno_a_prijmeni[1]

# všechna písmena velká (vypíše např. JANA MALÁ)
print("Převod na velká písmena:", jmeno.upper(), prijmeni.upper())

# všechna písmena malá (vypíše např. jana malá)
print("Převod na malá písmena:", jmeno.lower(), prijmeni.lower())

# standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
print("První písmeno velké, další malá:", jmeno.title(), prijmeni.title())

# iniciály (vypíše např. J. M.)
inicialy = jmeno[0] + ". " + prijmeni[0] + "."
print("Iniciály:", inicialy.upper())

# křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků.
# Jinak vypíše standardní variantu, tj. první písmeno velké, další malá
# (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)

if len(jmeno) > 5:
    print(f"Zkrácené jméno: {jmeno[0]}. {prijmeni}")
else:
    print(f"Celé jméno: {jmeno} {prijmeni}")