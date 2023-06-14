import re
import copy

lines = open("./inputs/24.txt").read().split("\n")
hexes, new_hexes = [], []
for line in lines:
    a, b, y = 0, 0, 0
    seq = re.findall(r'ne|nw|sw|se|e|w', line)
    for cmd in seq:
        if cmd == 'nw': a, y = a+1, y-1
        elif cmd == 'ne': b, y = b+1, y-1
        elif cmd == 'w': a, b = a+1, b-1
        elif cmd == 'e': a, b = a-1, b+1
        elif cmd == 'sw': b, y = b-1, y+1
        elif cmd == 'se': a, y = a-1, y+1
    if [a,b,y] not in hexes:
        hexes.append([a,b,y])
    else:
        hexes.remove([a,b,y])

def find_adj(a, b, y):
    adj = 0
    mods = [[1,0,-1],[0,1,-1],[1,-1,0],[-1,1,0],[0,-1,1],[-1,0,1]]
    for mod in mods:
        if [a+mod[0],b+mod[1],y+mod[2]] in hexes: adj+=1
    return adj

def flip_white(a, b, y):
    to_flip = []
    mods = [[1,0,-1],[0,1,-1],[1,-1,0],[-1,1,0],[0,-1,1],[-1,0,1]]
    for mod in mods:
        if [a+mod[0], b+mod[1], y+mod[2]] in hexes + new_hexes:
            continue
        if find_adj(a+mod[0],b+mod[1],y+mod[2]) == 2: to_flip.append([a+mod[0],b+mod[1],y+mod[2]])
    return to_flip

for i in range(100):
    new_hexes = []
    for aby in hexes:
        adj = find_adj(aby[0],aby[1],aby[2])
        if adj == 1 or adj == 2:
            new_hexes.append(aby)
        if adj <= 4:
            new_hexes += flip_white(aby[0],aby[1],aby[2])
    hexes = copy.deepcopy(new_hexes)
    print(i)
print(len(hexes))