tab = [int(i) for i in open("input8.txt").read().split(" ")]
somme_meta = 0
def f1(pos, nb_nodes, nb_meta):
    while nb_nodes > 0:
        pos = f1(pos+2, tab[pos], tab[pos+1])
        nb_nodes -= 1
    global somme_meta 
    somme_meta += sum(tab[pos+i] for i in range(nb_meta))
    return pos + nb_meta
f1(2,7,11)
print("Partie 1:", somme_meta)

def f2(pos, nb_nodes, nb_meta):
    nodes = []
    while nb_nodes > 0:
        pos, node_value = f2(pos+2, tab[pos], tab[pos+1])
        nodes = nodes + [node_value]
        nb_nodes -= 1
    if len(nodes) == 0:
        value = sum(tab[pos:pos+nb_meta])
    else:
        value = sum(nodes[i-1] for i in tab[pos:pos+nb_meta] if i<=len(nodes))
    return pos + nb_meta, value
print("Partie 2:", f2(2,7,11)[1])
