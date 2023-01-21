input = open("input.txt").read().splitlines()

res1 = 0
x = 1
j = 0
crt = ''

def draw_pixel(cycle, crt):
    pos = x + 40 * (cycle // 40)
    if abs(cycle - pos) <= 1:
        crt += "#"
    else:
        crt += '.'
    return crt

for i, ins in enumerate(input):
    if (i+j) % 40 == 19:
        res1 += x * (i+j+1)
    crt = draw_pixel(i+j, crt)
    if ins == "noop":
        continue
    j += 1
    crt = draw_pixel(i+j, crt)
    if (i+j) % 40 == 19:
        res1 += x * (i+j+1)
    x += int(ins[5:])

print(f"Partie 1: {res1}")
print("Partie 2:")
for i in range(6):
    print(crt[40*i:40*(i+1)])