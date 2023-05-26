instructions = [l.rstrip('\n') for l in open('./inputs/12.txt')]
isPartOne = False
xpos, ypos = 0 if isPartOne else 10, 0 if isPartOne else 1
shipx, shipy = 0, 0
dir = 1
xmod, ymod = [0, 1, 0, -1], [1, 0, -1, 0]
dirs = {'N':0, 'E':1, 'S':2, 'W':3}

def rotate(w, d):
    global xpos, ypos, shipx, shipy
    if isPartOne:
        global dir
        dir += int(w/90) * d
    else:
        coords = [0, xpos-shipx, ypos-shipy]
        mods = [[],[0,1,-1,-1],[0,-1,-1,1]]
        xpos = mods[d][int(w/90)] * coords[pow(-1,int(w/90))] + shipx
        ypos = mods[-1*d][int(w/90)] * coords[pow(-1,int(w/90))*2] + shipy

for instruction in instructions:
    if instruction[0] == 'L' or instruction[0] == 'R':
        rotate(int(instruction[1:]), -1 if instruction[0] == 'L' else 1)
    elif instruction[0] == 'F':
        if isPartOne:
            xpos += xmod[dir%4] * int(instruction[1:])
            ypos += ymod[dir%4] * int(instruction[1:])
        else:
            for i in range(int(instruction[1:])):
                dx, dy = xpos-shipx, ypos-shipy
                shipx, shipy, xpos, ypos = xpos, ypos, xpos + dx, ypos + dy
    else:
        xpos += xmod[dirs.get(instruction[0])] * int(instruction[1:])
        ypos += ymod[dirs.get(instruction[0])] * int(instruction[1:])
print(abs(xpos) + abs(ypos) if isPartOne else abs(shipx) + abs(shipy))