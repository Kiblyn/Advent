import numpy as np
input = np.array([[int(x) for x in l] for l in open("input.txt").read().splitlines()])
visible = np.full_like(input, False)
scores = np.ones_like(input)

for _ in range(4):
    for i, l in enumerate(input):
        tallest = l[0]
        visible[i, 0] = True
        for j, x in enumerate(l):
            if j == 0:
                scores[i, j] = 0
                continue
            if x > tallest:
                visible[i, j] = True
                tallest = x
            k = j+1
            while k < len(l)-1 and l[k] < x:
                k += 1
            scores[i, j] *= k-j
    input = np.rot90(input)
    visible = np.rot90(visible)
    scores = np.rot90(scores)

res1 = np.sum(visible)
res2 = np.max(scores)

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")