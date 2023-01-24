import numpy as np
from itertools import combinations
isPartOne = False
data = np.loadtxt('./inputs/1.txt', dtype=int)
if (isPartOne):
    print(np.prod(list(filter(lambda x: x[0] + x[1] == 2020, list(combinations(data, 2))))))
else:
    print(np.prod(list(filter(lambda x: x[0] + x[1] + x[2] == 2020, list(combinations(data, 3))))))