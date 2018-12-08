lignes = open("input.txt").read().splitlines()
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tab = list((ligne[5], ligne[36]) for ligne in lignes)
requis = {x:[y[0] for y in tab if y[1]==x] for x in lettres}
resultat = ""
while len(resultat) < 26:
    for c in lettres:
        if c in resultat: continue
        if all((r in resultat) for r in requirements[c]):
            resultat += c
            break

print("Partie 1:", resultat)

temps_travail = [1]*5
unite_travail = ["" for _ in range(5)]
utilises = set()
finis = set()
compteur = 0
while temps_travail != [0]*5 :
    temps_travail = [max(i-1,0) for i in temps_travail]
    for i, temps in enumerate(temps_travail):
        if temps == 0:
            finis.add(unite_travail[i])
    disponibles = sorted(x for x in lettres if x not in utilises and all(y in finis for y in requis[x]))
    for i, temps in enumerate(temps_travail):
        if temps == 0 and len(disponibles) > 0:
            unite_travail[i] = disponibles[0]
            temps_travail[i] = ord(disponibles[0])-4
            utilises.add(disponibles.pop(0))
    compteur += 1
print("Partie 2:", compteur - 1)
