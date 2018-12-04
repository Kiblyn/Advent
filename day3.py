from itertools import product
from collections import defaultdict

total = 0
claim = defaultdict(set)
points = defaultdict(int)
conflits = set()

for i, l in enumerate(open("input3.txt").read().splitlines()):
    val = list(map(int, l.split(" ")[2][:-1].split(",") + l.split(" ")[3].split("x")))
    for point in [(val[0]+i)*1000+val[1]+j for i,j in product(range(val[2]), range(val[3]))]:
        points[point] += 1
        claim[point].add(i+1)
        if points[point] == 2: total += 1
        if len(claim[point]) > 1: conflits = conflits.union(claim[point])

print("Partie 1:", total)
print("Partie 2:", set(range(1,1336)) - conflits)
