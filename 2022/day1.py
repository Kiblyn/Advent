input = open("input.txt").read()
elves = sorted((sum(map(int, x.splitlines())) for x in input.split('\n\n')), reverse=True)

res1 = elves[0]
res2 = sum(elves[:3])

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")