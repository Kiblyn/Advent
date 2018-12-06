points = []
for ligne in open("input6.txt").read().splitlines():
    points.append([int(x) for x in ligne.split(", ")])
nb_points = [0]*len(points)
nb_region = 0
bords_x = [min(points[i][0] for i in range(len(points)))-1, max(points[i][0] for i in range(len(points)))+2]
bords_y = [min(points[i][1] for i in range(len(points)))-1, max(points[i][1] for i in range(len(points)))+2]
dist_point = lambda i:abs(x - points[i][0])+abs(y - points[i][1])

for x in range(0, 361):
    for y in range(0, 361):
        nb_region += int(sum(dist_point(i) for i in range(len(points))) < 10000)
        indices = sorted(range(len(points)), key=dist_point)
        if dist_point(indices[0]) == dist_point(indices[1]): continue
        nb_points[indices[0]] += 1
        if x in bords_x or y in bords_y:
            nb_points[indices[0]] = -1000000

print("Partie 1:", max(nb_points))
print("Partie 2:", nb_region)
