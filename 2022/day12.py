import numpy as np
input = np.array([[ord(c)-97 for c in l] for l in open("input.txt").read().splitlines()])
end = np.unravel_index(np.argmin(input), input.shape)
start = (20, 0)
input[start], input[end] = 0, 25
distances = np.zeros_like(input)

def voisins(sq, shape):
    i, j = sq
    voisins = []
    if i-1 >= 0:
        voisins.append((i-1, j))
    if j-1 >= 0:
        voisins.append((i, j-1))
    if i+1 < shape[0]:
        voisins.append((i+1, j))
    if j+1 < shape[1]:
        voisins.append((i, j+1))
    return voisins

next = set()
next.add(end)
d = 0
while len(next) > 0:
    new_next = set()
    for sq in list(next):
        distances[sq] = d
        height = input[sq]
        for voisin in voisins(sq, input.shape):
            if voisin == end:
                continue
            if distances[voisin] == 0 and height < (input[voisin] + 2):
                new_next.add(voisin)
    next = new_next
    d += 1

res1 = distances[start]
res2 = np.min([x for x in distances[input == 0] if x])

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")