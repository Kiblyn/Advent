nb_2 = 0
nb_3 = 0
for ligne in open("input2.txt", 'r'):
    ligne_2 = 0
    ligne_3 = 0
    for c in set(ligne):
        if ligne.count(c) == 2 and not ligne_2:
            ligne_2 = 1
        elif ligne.count(c) == 3 and not ligne_3:
            ligne_3 = 1
    nb_2 += ligne_2
    nb_3 += ligne_3
    
print("Partie 1:", nb_2*nb_3) 
    
for couple_ligne in product(open("input2.txt", 'r'), repeat=2):
    nb = 0
    for i,c in enumerate(couple_ligne[0]):
        if couple_ligne[1][i] != c:
            nb += 1
            if nb == 2:
                break
    if nb == 1:
        print("Partie 2:", couple_ligne)
        break
