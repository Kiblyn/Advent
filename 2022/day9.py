import numpy as np
input = open("input.txt").read().splitlines()
tail = (0, 0)
head = (0, 0)
pos1 = set()
pos1.add((0, 0))

moves = ''
for l in input:
    dir, d = l.split(" ")
    moves += dir * int(d)

def move_head(head, move):
    head_x, head_y = head
    if move == "U":
        head_y += 1
    elif move == "R":
        head_x += 1
    elif move == "D":
        head_y -= 1
    else:
        head_x -= 1
    return head_x, head_y

def follow(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    if (abs(tail_y - head_y) > 1 or abs(tail_x - head_x) > 1):
        if tail_y < head_y:
            tail_y += 1
        if tail_x < head_x:
            tail_x += 1
        if tail_y > head_y:
            tail_y -= 1
        if tail_x > head_x:
            tail_x -= 1
    return tail_x, tail_y

for move in moves:
    head = move_head(head, move)
    tail = follow(head, tail)
    pos1.add(tail)

pos2 = set()
pos2.add((0, 0))
knots = np.zeros((10, 2))

for move in moves:
    knots[0] = move_head(knots[0], move)
    for i in range(9):
        knots[i+1] = follow(knots[i], knots[i+1])
    tail_x, tail_y = knots[9]
    pos2.add((tail_x, tail_y))

res1 = len(pos1)
res2 = len(pos2)

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")