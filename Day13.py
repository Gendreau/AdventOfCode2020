import numpy as np

n, *b = open("./inputs/13.txt")
buses = np.genfromtxt(b, delimiter=',', dtype=int, loose=True)
n = int(n)
wait = {}
for bus in buses:
    if bus>0:
        wait[bus-(n%bus)] = bus
print(min(wait.keys()) * wait[min(wait.keys())])

for i, n in enumerate(buses):
    if n > 0:
        print('(t+%d) mod %d = 0, ' % (i,n), end="")