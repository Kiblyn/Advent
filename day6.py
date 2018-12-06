points = [[int(x) for x in ligne.split(", ")] for ligne in open("input6.txt").read().splitlines()]
nb_points = [0]*len(points)
nb_region = 0
bords_x = [min(x[0] for x in points)-1, max(x[0] for x in points)+2]
bords_y = [min(x[1] for x in points)-1, max(x[1] for x in points)+2]
dist_point = lambda i:abs(x - points[i][0])+abs(y - points[i][1])

for x in range(bords_x[0], bords_x[1]):
    for y in range(bords_y[0], bords_y[1]):
        nb_region += int(sum(dist_point(i) for i in range(len(points))) < 10000)
        indices = sorted(range(len(points)), key=dist_point)
        if dist_point(indices[0]) == dist_point(indices[1]): continue
        nb_points[indices[0]] += 1
        if x in bords_x or y in bords_y:
            nb_points[indices[0]] = -1000000

print("Partie 1:", max(nb_points))
print("Partie 2:", nb_region)
