lst = [-1, -5, -3,9]

def som_negatief(getallen):
    som =0
    for getal in getallen:
        if getal < 0:
           som = som + getal
    return som

a = som_negatief(lst)

print(a)
print(a == -9)

def wijzig(lijst2):
    # lijst2=['e','f','g']
    lijst2.clear()
   # lijst2[2] = 'f'

wijzig(lst)
print(lst)
