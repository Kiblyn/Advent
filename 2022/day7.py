class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.children = {}
        self.parent = parent
        self.size = 0
        if parent is not None:
            parent.add_child(self)

    def add_child(self, child):
        self.children[child.name] = child
        if child.size > 0:
            self.update_size(child.size)
        

    def update_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.update_size(size)


class File:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size
        parent.add_child(self)
    
input = open("input.txt").read().splitlines()

root = Folder('/', None)
dirs = [root]
curr_dir = root
for line in input[2:]:
    ins = line[:3]
    if ins == "$ l":
        continue
    if ins == "$ c":
        dir_name = line[5:]
        if dir_name == "..":
            curr_dir = curr_dir.parent
        else :
            curr_dir = curr_dir.children[dir_name]
    elif ins == "dir":
        dirs.append(Folder(line[4:], curr_dir))
    else :
        size, name = line.split(" ")
        f = File(name, curr_dir, int(size))

req_size = root.size - 40000000

res1 = sum(d.size for d in dirs if d.size <= 100000)
res2 = min(d.size for d in dirs if d.size >= req_size)

print(f"Partie 1: {res1}")
print(f"Partie 2: {res2}")