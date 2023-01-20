input = open("input.txt").read()

for i, c in enumerate(input[3:]):
    prev = set(c for c in input[i:i+3])
    if len(prev) < 3:
        continue
    if c not in prev:
        res1 = i + 4
        break

for i, c in enumerate(input[13:]):
    prev = set(c for c in input[i:i+13])
    if len(prev) < 13:
        continue
    if c not in prev:
        res2 = i + 14
        break

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")