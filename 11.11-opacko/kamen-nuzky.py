import random

pocitac_vyber = random.choice(["kamen", "nuzky", "papir"])

hrac_vyber = input()

if (pocitac_vyber == hrac_vyber):
    print("remiza")

elif (hrac_vyber == "kamen"):
    if (pocitac_vyber == "nuzky"):
        print("vyhral jsi")

    elif (pocitac_vyber == "papir"):
        print("prohral jsi")

elif (hrac_vyber == "nuzky"):
    if (pocitac_vyber == "papir"):
        print("vyhral jsi")

    elif (pocitac_vyber == "kamen"):
        print("prohral jsi")

elif (hrac_vyber == "papir"):
    if (pocitac_vyber == "kamen"):
        print("vyhral jsi")

    elif (pocitac_vyber == "nuzky"):
        print("prohral jsi")

print("pocitac zahral:", pocitac_vyber)