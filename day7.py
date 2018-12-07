lignes = open("input.txt").read().splitlines()
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tab = list((ligne[5], ligne[36]) for ligne in lignes)
requirements = {x:[y[0] for y in tab if y[1]==x] for x in lettres}
resultat = ""
while len(resultat) < 26:
    for c in lettres:
        if c in resultat: continue
        if all((r in resultat) for r in requirements[c]):
            resultat += c
            break

print("Partie 1:", resultat)
