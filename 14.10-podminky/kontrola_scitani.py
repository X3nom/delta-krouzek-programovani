prvni_cislo = int(input("prvni cislo: "))
druhe_cislo = int(input("druhe cislo: "))

vysledek = int(input("tvuj vysledek: "))

opravdovy_vysledek = prvni_cislo + druhe_cislo

if vysledek == opravdovy_vysledek:
    print("Spravne!")

else:
    print("Neumis pocitat")

'''
int = integer = cele cislo (Jde sčítat a odečítat)
str = string = text (Nedá se sčítat a odečítat ale můžou v něm být písmena)
bool = boolean = pravda/nepravda (True/False) (To je to co vám dá podmínka např:.

i = 1

i == 1 --> True(Pravda)

'''