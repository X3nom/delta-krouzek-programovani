
# auto = [poskozeni, barva, model, cena, SPZ, majitel]

autoservis = []

def pridej_auto():
    poskozeni = input("Zadejte poškození auta: ")
    barva = input("Zadejte barvu auta: ")
    model = input("Zadejte model auta: ")
    cena = input("Zadejte cenu auta: ")
    SPZ = input("Zadejte SPZ auta: ")
    majitel = input("Zadejte majitele auta: ")

    return [poskozeni, barva, model, cena, SPZ, majitel]

def napoveda():
    print("1 - Přidání auta")
    print("2 - Odebrání auta")
    print("3 - Změnit auto")
    print("4 - Vypsat auta")
    print("help - Vypíše tuhle nápovědu")
    print("exit - Ukončí program")

def vypsat_auta(autoservis):
    for i in range(len(autoservis)):
        print("Poškození auta číslo:" + str(i) + ": " + autoservis[i][0])
        print("Barva auta číslo " + str(i) + ": " + autoservis[i][1])
        print("Model auta číslo " + str(i) + ": " + autoservis[i][2])
        print("Cena auta číslo " + str(i) + ": " + autoservis[i][3])
        print("SPZ auta číslo " + str(i) + ": " + autoservis[i][4])
        print("Majitel auta číslo " + str(i) + ": " + autoservis[i][5])


napoveda()

while True:
    vstup = input("Jakou akci chete dělat? ")

    if vstup == "help":
        napoveda()
    elif vstup == "1":
        autoservis.append(pridej_auto())
    elif vstup == "4":
        vypsat_auta(autoservis)
    elif vstup == "exit":
        break
    elif vstup == "help":
        napoveda()