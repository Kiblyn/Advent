input = open("input.txt").read().splitlines()
letters = [set(s[:len(s)//2]).intersection(set(s[len(s)//2:])).pop() for s in input]
badges = [set(input[i]).intersection(set(input[i+1])).intersection(set(input[i+2])).pop() for i in range(0, len(input), 3)]

res1 = sum(ord(c) - 38 if c.isupper() else ord(c) - 96 for c in letters)
res2 = sum(ord(c) - 38 if c.isupper() else ord(c) - 96 for c in badges)

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")