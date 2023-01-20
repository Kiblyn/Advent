nb_joueurs = 439
bille_max = 7130700
class bille:
    def __init__(self, val, prec=None, suiv=None):
        self.val = val
        self.prec = prec
        self.suiv = suiv
n = 1
curr = bille(0)
curr = bille(1, curr, curr)
curr.prec.suiv = curr
curr.suiv.prec = curr
scores = [0]*nb_joueurs
tour = 0
while n < bille_max:
    n += 1
    if n % 23 == 0:
        curr = curr.prec.prec.prec.prec.prec.prec.prec
        curr.prec.suiv = curr.suiv
        curr.suiv.prec = curr.prec
        scores[tour] += n + curr.val
        tour = (tour + 1)%439
        curr = curr.suiv
    else:
        curr = bille(n, curr.suiv, curr.suiv.suiv)
        curr.prec.suiv = curr
        curr.suiv.prec = curr
print(max(scores))
