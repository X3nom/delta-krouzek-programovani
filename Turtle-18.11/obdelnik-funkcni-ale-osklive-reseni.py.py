import turtle

strana_a = int(input("zadej velikost strany a:"))
strana_b = int(input("zadej velikost strany b:"))


# Manualne napsany kazdy pohyb, ktery zelva udela.
# Pro obdelnik je to mozne napsat docela jednodusse a citelne, co kdybychom ale chteli kresli napriklad 8-úhelník?
# V tu cvili se vyplati vyuzit while loop (příkladový program je v souboru obdelnik-reseni.py)
turtle.forward(strana_a)
turtle.left(90)
turtle.forward(strana_b)
turtle.left(90)
turtle.forward(strana_a)
turtle.left(90)
turtle.forward(strana_b)
turtle.left(90)


    
# input je zde pouze proto, aby program cekal a neukoncil se po dokresleni (coz by zavrelo okno i s tim, co jsme nakreslili)
input()