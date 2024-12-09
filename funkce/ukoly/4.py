def vydel(cislo1, cislo2):
    if (cislo2 == 0):
        return "Nelze delit nulou"
    podil=cislo1/cislo2
    return podil

print(vydel(1, 2))