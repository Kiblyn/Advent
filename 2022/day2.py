import pandas as pd

df = pd.read_csv("input.txt", header=None, sep=' ')
df[1] = [ord(x)-87 for x in df[1]]
df[0] = [ord(x)-64 for x in df[0]]
df["diff"] = (df[1] - df[0]) % 3
df["score"] = (df["diff"] + 1) % 3 * 3 + df[1]

score_lose = sum((df[0][df[1] == 1] - 2) % 3 + 1)
score_draw = sum(df[0][df[1] == 2] + 3)
score_win = sum(df[0][df[1] == 3] % 3 + 7)

res1 = sum(df["score"])
res2 = score_lose + score_draw + score_win

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")