# Zadani

"""
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. 
Napiš program, který provede následující činnosti:

1. Zeptá se uživatele na číslo, kam chce zprávu zaslat 
a ověří, že číslo má správný formát.
2. Zeptá se uživatele na zprávu, kterou chce zaslat. 
Následně vypíše, kolik zpráva bude stát.

Tvůj program bude obsahovat dvě funkce:

1. První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo 
může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). 
Funkce ověří, jestli je číslo platné. Pokud je platné, 
vrátí hodnotu True, jinak vrátí hodnotu False.

2. Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč 
za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost 
telefonního čísla. Pokud není platné, vypíše chybu, 
v opačném případě se zeptá na text zprávy a 
pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:

Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, 
či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) 
pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".

# BONUS 1

Zkus svoji první funkci upravit tak, že si bude umět poradit 
s mezerami v telefonním čísle. Mezer se zbavíš například tak, 
že použiješ metodu .replace(). První parametr metody replace je znak, 
který chceš nahradit, a druhý parametr nový znak. 
Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".

# BONUS 2

Přidej svým funkcím typování, aby bylo jasné, 
jaký typy mají parametry tvých funkcí a jaká je návratová hodnota tvých funkcí.
"""


def verify_phone_number(phone_number: str) -> bool:
    """Check if the phone number has a correct format - nine-digit
    or thirteen-digit if including an area code.

    Arguments:
    phone_number (str): the phone number entered by the user
    Returns:
    bool: True if the phone number is correct, False otherwise.
    """
    if len(phone_number) == 9 or (len(phone_number) == 13 and phone_number[:4] == "+420"):
        return True
    else:
        return False

def calculate_price(text: str, msg_price = 3) -> int:
    """Calculate the total cost of the entered text message. 
    Every 180 characters of the message costs 3 czech crowns.
    
    Arguments:
    text (str): a text message entered by the user
    msg_price (int): the price for every 180 characters of the message (default: 3)
    Returns:
    total_price (int): the total cost of the text message
    """

    if len(text) % 180 == 0:
        total_price = (len(text) / 180) * msg_price
    else:
        total_price = (len(text) // 180 + 1) * msg_price
    return total_price

user_phone_number = input(str("Zadej číslo, kam chceš zaslat zprávu: ")).replace(" ", "")
if verify_phone_number(user_phone_number):
    user_text = input("Napiš text zprávy: ")
    print(f"Zpráva stoji {calculate_price(user_text, msg_price = 3)} kč.")
else:
    print("Číslo není platné!")
