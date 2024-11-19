import turtle # je nutne, aby jsme turtle mohli pouzit


# Ziskame od uzivatele vstup, jak velke maji byt strany a zapiseme ho do promennych
strana_a = int(input("zadej stranu a: "))
strana_b = int(input("zadej stranu b: "))


i = 0 # i pouzijeme jako pocitadlo, kolikrat jsme jiz nakreslili strany

# bude se opakovat 2x, protoze pri kazdem pruchodu se nakresli 2 strany a mi potrebujeme nakreslit 4
while i<2:
    turtle.forward(strana_a)
    turtle.left(90)
    turtle.forward(strana_b)
    turtle.left(90)

    i = i + 1 # zvysyme pocitadlo o 1

    
# input je zde pouze proto, aby program cekal a neukoncil se po dokresleni (coz by zavrelo okno i s tim, co jsme nakreslili)
input()