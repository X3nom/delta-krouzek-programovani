seznam = [] # Vytvor prazdny seznam

while True: # Dokud uzivatel nezada prazdny radek
    cislo = input() # Ziskej vstup od uzivatele
    if cislo == "": # Pokud uzivatel zada prazdny radek
        break # Ukonci cyklus
    seznam.append(int(cislo)) # Pridat cislo do seznamu