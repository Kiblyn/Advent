sommes = []
for y in range(300):
    sommes.append([0])
    for x in range(300):
        sommes[y].append(sommes[y][-1]+(((x+10)*y+9110)*(x+10)//100)%10-5)

maxi = 0
nmax = 0
for n in range(3,60):
    for y in range(301-n):
        for x in range(301-n):
            s = sum(sommes[y][x+n]-sommes[y][x] for y in range(y, y+n))
            if s > maxi:
                maxi = s
                pos = (x,y)
                nmax = n
    if n == 3:
        res = pos
    if n>nmax+5:
        break
print("Partie 1:", res)
print("Partie 2:", pos, nmax)
