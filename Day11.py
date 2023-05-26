lines = [l.rstrip('\n') for l in open('./inputs/11.txt')]
lines_clone = []
isPartOne = True
occs_to_move = 4 if isPartOne else 5

def check(i, j):
    totalOcc = 0
    dirs = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    for n in dirs:
        totalOcc += look(i + n[0], j + n[1], n[0], n[1])
    return totalOcc

def look(i, j, dy, dx):
    if i < 0 or j < 0 or i > len(lines)-1 or j > len(lines[i])-1:
        return 0
    if lines_clone[i][j] == '.' and not isPartOne:
        return look(i+dy,j+dx,dy,dx)
    else:
        return 1 if lines_clone[i][j] == '#' else 0

while (lines != lines_clone):
    lines_clone = lines.copy()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines_clone[i][j] == 'L' and check(i,j) == 0:
                try: lines[i] = lines[i][:j] + "#" + lines[i][j+1:]
                except: lines[i] = lines[i][:j] + "#"
            elif lines_clone[i][j] == '#' and check(i, j) >= occs_to_move:
                try: lines[i] = lines[i][:j] + "L" + lines[i][j+1:]
                except: lines[i] = lines[i][:j] + "L"

print(sum([line.count('#') for line in lines]))