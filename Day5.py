import math
seatIDs = []
with open("./inputs/5.txt") as f:
    for line in f.readlines():
        min = 0
        maxi = 127
        for index, char in enumerate(line.strip()):
            if char == 'F' or char == 'L':
                maxi = math.floor((maxi+min)/2)
            elif char == 'B' or char == 'R':
                min = math.ceil((maxi+min)/2)
            if index == 6:
                row = min
                min = 0
                maxi = 7
        seatIDs.append(row*8+min)
print(max(seatIDs))
seatIDs.sort()
for i in range(1, len(seatIDs)):
    if seatIDs[i]-seatIDs[i-1] != 1:
        print(seatIDs[i]-1)