import re
input = open("input.txt").read().splitlines()
input = [list(map(int, re.split('-|,', x))) for x in input]

res1 = sum(1 for x in input if (x[0] <= x[2] and x[1] >= x[3]) or (x[2] <= x[0] and x[3] >= x[1]))
res2 = sum(1 for x in input if not (x[1] < x[2] or x[0] > x[3]))

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")