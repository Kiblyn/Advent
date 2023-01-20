points = [(int(l[10:16]), int(l[18:24])) for l in open("input10.txt").read().splitlines()]
vitesses = [(int(l[36:38]), int(l[40:42])) for l in open("input10.txt").read().splitlines()]

def next_points(n):
    for i, (p,v) in enumerate(zip(points, vitesses)):
        points[i] = p[0] + n*v[0], p[1] + n*v[1]
next_points(10000)
n=10000
total = 1
while total != 0:
    n+=1
    next_points(1)
    total = sum(min(max(abs(p[0] - c[0]),abs(p[1] - c[1]))-1 for c in points if c!=p) for p in points)
print("Partie 1:")
for y in range(min(p[1] for p in points), max(p[1] for p in points)+1):
    for x in range(min(p[0] for p in points), max(p[0] for p in points)+1):
        if (x,y) in points:
            print('#', end='')
        else:
            print('.', end='')
    print('')
print("Partie 2:", n)
