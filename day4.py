from collections import defaultdict

tab = sorted(open("input4.txt").read().splitlines())
sommeil = defaultdict(int)
minutes = dict()

def hash_date(h):
    jours_mois = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    ha = 60 * (24 * (jours_mois[int(h[6:8])-1] + (int(h[9:11])-1)) + int(h[12:14])) + int(h[15:17])
    return ha
    
for i, ligne in enumerate(tab):
    if '#' in ligne:
        garde = int((ligne.split(' ')[3][1:]))
        if garde not in minutes:
            minutes[garde] = defaultdict(int)
    elif ligne[-2:] == "ep":
        deb = hash_date(ligne)
        fin = hash_date(tab[i+1])
        sommeil[garde] += (fin - deb)
        for i in range(deb%1440, fin%1440):
            minutes[garde][i] += 1
        
garde_max = max(sommeil, key=lambda x: sommeil[x])
min_max = max(minutes[garde_max], key=lambda x:minutes[garde_max][x])
t = list((i, max(minutes[i], key=lambda x:minutes[i][x], default=0), max(minutes[i].values(), default=0)) for i in minutes)
r = max(t, key=lambda x: x[2])

print("Partie 1:", garde_max * min_max)
print("Partie 2:", r[0]*r[1])
