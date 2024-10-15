bohaty = True
mlady = True



if mlady == True or (bohaty == True and mlady == False):
    print("ano")
else:
    print("ne")






'''
# alternativni reseni:

if mlady == True:
    print("ano")

else:
    if bohaty == True and mlady == False:
        print("ano")
    else:
        print("ne")
'''