sommes = [[0]*301]
for y in range(1,301):
    sommes.append([0])
    for x in range(1,301):
        sommes[y].append(sommes[y-1][x]+sommes[y][x-1]-sommes[y-1][x-1]+(((x+10)*y+9110)*(x+10)//100)%10-5)
maxi = 0
nmax = 0
for n in range(3,301):
    for y in range(1,301-n):
        for x in range(1,301-n):
            s = sommes[y-1][x-1]+sommes[y+n-1][x+n-1]-sommes[y+n-1][x-1]-sommes[y-1][x+n-1]
            if s > maxi:
                maxi = s
                pos = (x,y)
                nmax = n
    if n == 3:
        res = pos
print("Partie 1:", res)
print("Partie 2:", pos, nmax)
