input = open("input.txt").read().splitlines()
monkeys = [list(map(int, l[18:].split(", "))) for i, l in enumerate(input) if i % 7 == 1]
div = [int(l[21:]) for i, l in enumerate(input) if i % 7 == 3]
options = [(int(input[i][29]), int(input[i+1][30])) for i in range(len(input)) if i % 7 == 4]
inspections = [0]*8
print(monkeys)

def turn(n, item, bored=True):
    inspections[n] += 1
    if n == 0:
        item *= 13
    elif n == 1:
        item *= item
    elif n == 2:
        item += 7
    elif n == 3:
        item += 4
    elif n == 4:
        item *= 19
    elif n == 5:
        item += 3
    elif n == 6:
        item += 5
    else:
        item += 1
    if bored:
        item //= 3
    else:
        item %= (2*3*5*7*11*13*17*19)
    opt1, opt2 = options[n]
    m = opt2 if item % div[n] else opt1
    monkeys[m].append(item)


for _ in range(20):
    for n in range(len(monkeys)):
        for item in monkeys[n]:
            turn(n, item)
        monkeys[n] = []

inspections = sorted(inspections, reverse=True)
res1 = inspections[0] * inspections[1]

inspections = [0]*8
monkeys = [list(map(int, l[18:].split(", "))) for i, l in enumerate(input) if i % 7 == 1]
print(monkeys)
for _ in range(10000):
    for n in range(len(monkeys)):
        for item in monkeys[n]:
            turn(n, item, False)
        monkeys[n] = []

inspections = sorted(inspections, reverse=True)
res2 = inspections[0] * inspections[1]
print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")