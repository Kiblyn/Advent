from itertools import cycle

ite = map(int, cycle(open("input.txt").read().splitlines()))
valeurs = set()
somme = next(ite)

while somme not in valeurs:
    valeurs.add(somme)
    somme += next(ite)

print("Partie 1:", eval('0'+''.join(open("input.txt").read().splitlines())))
print("Partie 2:", somme)
