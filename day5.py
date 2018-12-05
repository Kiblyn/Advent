def full_react(tab):
    different = True
    while different:
        i = 0
        different = False
        while i < len(tab) - 1:
            if tab[i] != tab[i+1] and tab[i].lower() == tab[i+1].lower():
                tab.pop(i)
                tab.pop(i)
                different = True
            else:
                i += 1
    return len(tab)

tab = [c for c in open("input5.txt").read()]
print("Partie 1:", full_react(tab))
print("Partie 2:", min(full_react(t) for t in [[c for c in tab if c.lower()!=a] for a in "abcdefghijklmnopqrtstuvwxyz"]))
