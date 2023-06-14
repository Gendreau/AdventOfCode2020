import re
import math

# Parses input
lines = open('./inputs/test.txt').read().strip().split('\n\n')
fields, ranges = re.findall(r'\d+', lines[0]), []
for x in range(1,len(fields),2):
    ranges.append([int(fields[x-1]),int(fields[x])])
ticket = re.findall(r'\d+', lines[1])
nearbys = [x.split(',') for x in re.split('nearby tickets:\n|\n',lines[2])[1:]]
nearbys = [[int(x) for x in y] for y in nearbys]

# Finds every line containing a number that fits in no ranges and saves both the line number and invalid number
invalids, to_delete = [], []
for i, nearby in enumerate(nearbys):
    for x in nearby:
        if (any(y[0] <= x <= y[1] for y in ranges)):
            continue
        else:
            invalids.append(x)
            to_delete.append(i)
            break
print(sum(invalids))

# Deletes lines with invalid numbers
for i in reversed(to_delete):
    nearbys.remove(nearbys[i])

# For every digit place x_i, generates a list of ranges in which the number in that place for line x fits
# Between lines, saves only the intersection between the master list of valid ranges and line x's valid ranges
potential = [set(range(int(len(ranges)/2))) for _ in range(int(len(ranges)/2))]
for nearby in nearbys:
    subpot = [set() for _ in range(int(len(ranges)/2))]
    for x_i, x in enumerate(nearby):
        for y_i, y in enumerate(ranges):
            if y[0] <= x <= y[1]: subpot[x_i].add(math.floor(y_i/2))
    for i in range(int(len(ranges)/2)):
        potential[i] = potential[i] & subpot[i] 
    if all(len(x) == 1 for x in potential):
        break

# Uses process of elimination to find the exact correlation between range and digit place
solution = [-1 for _ in range(len(potential))]
while any(x == -1 for x in solution):
    for p in range(len(potential)):
        if len(potential[p]) == 1:
            to_delete = list(potential[p])[0]
            solution[p] = to_delete
            for pp in range(len(potential)):
                if to_delete in potential[pp]: potential[pp].remove(to_delete)
            break

# Finds product of the values matching the first 6 ranges
total = 1
for i, x in enumerate(solution):
    if x < 6:
        total *= int(ticket[i])
print(total)