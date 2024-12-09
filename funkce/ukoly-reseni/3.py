def je_sude(cislo):
    return cislo % 2 == 0

'''
Jde zapsat také jako:

def je_sude(cislo):
    if cislo % 2 == 0:
        return True
    else:
        return False
        
u True a False nemusí být uvozovku protože to vracím jako logickou hodnotu a ne jako slovo(string) u jiných slov by toto nešlo
'''

print(je_sude(0)) # True
print(je_sude(3)) # False
print(je_sude(10)) # True