instructions = [l.rstrip('\n') for l in open('./inputs/12.txt')]
isPartOne = True
xpos = 0 if isPartOne else 10
ypos = 0 if isPartOne else 1
shipx = 0
shipy = 0
dir = 1
xmod = [0, 1, 0, -1]
ymod = [1, 0, -1, 0]

def rotate(w, d):
    global xpos
    global ypos
    global shipx
    global shipy
    if isPartOne:
        global dir
        dir += int(w/90) * d
        if dir < 0: dir += 4
        elif dir > 3: dir -= 4
    else:
        if w == 90:
            tmpx = xpos - shipx
            tmpy = ypos - shipy
            xpos = (tmpy * d) + shipx
            ypos = (tmpx * d * -1) + shipy
        elif w == 180:
            xpos = -1 * (xpos-shipx) + shipx
            ypos = -1 * (ypos-shipy) + shipy
        elif w == 270:
            rotate(90, d*-1)

for instruction in instructions:
    if instruction[0] == 'N':
        ypos += int(instruction[1:])
    elif instruction[0] == 'S':
        ypos -= int(instruction[1:])
    elif instruction[0] == 'E':
        xpos += int(instruction[1:])
    elif instruction[0] == 'W':
        xpos -= int(instruction[1:])
    elif instruction[0] == 'L':
        rotate(int(instruction[1:]), -1)
    elif instruction[0] == 'R':
        rotate(int(instruction[1:]), 1)
    elif instruction[0] == 'F':
        if isPartOne:
            xpos += xmod[dir] * int(instruction[1:])
            ypos += ymod[dir] * int(instruction[1:])
        else:
            for i in range(int(instruction[1:])):
                movex = xpos - shipx
                movey = ypos - shipy
                shipx = xpos
                shipy = ypos
                xpos += movex
                ypos += movey
print(abs(xpos) + abs(ypos) if isPartOne else abs(shipx) + abs(shipy))