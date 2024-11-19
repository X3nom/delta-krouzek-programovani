import turtle # je nutne, aby jsme turtle mohli pouzit


# Ziskame od uzivatele vstup, jak velke maji byt strany a zapiseme ho do promennych
strana_a = int(input("zadej stranu a: "))
strana_b = int(input("zadej stranu b: "))


# Bude se opakovat do nekonecna
while True:
    # nakresli stranu a a otoci se do leva
    turtle.forward(strana_a)
    turtle.left(90)
    # nakresli stranu b
    turtle.forward(strana_b)
    turtle.left(90)


# Pokud by jsme nechteli, aby zelva jezdila do nekonecna, reseni je v "obdelnik-reseni-verze-2.py"