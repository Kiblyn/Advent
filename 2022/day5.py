input = open("input.txt").read().splitlines()
stacks = [[input[i][4*j+1] for i in range(8) if input[i][4*j+1]!=' '] for j in range(9)]
steps = [l.split(' ') for l in input[10:]]
steps = [(int(x[1]), int(x[3]), int(x[5])) for x in steps]
stacks2 = stacks[:]

for n, x, y in steps:
    x, y = x-1, y-1
    n = min(n, len(stacks[x]))
    stacks[y] = stacks[x][n-1::-1] + stacks[y]
    stacks2[y] = stacks2[x][:n] + stacks2[y]
    stacks[x] = stacks[x][n:]
    stacks2[x] = stacks2[x][n:]

res1 = ''.join([stack[0] for stack in stacks if len(stack) > 0])
res2 = ''.join([stack[0] for stack in stacks2 if len(stack) > 0])

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")