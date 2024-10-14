prvni_cislo = int(input("prvni cislo: "))
druhe_cislo = int(input("druhe cislo: "))

vysledek = int(input("tvuj vysledek: "))

opravdovy_vysledek = prvni_cislo + druhe_cislo

if vysledek == opravdovy_vysledek:
    print("Spravne!")

else:
    print("Neumis pocitat")