import numpy as np
import re

data = []
with open('./inputs/test.txt') as f:
    for line in f.readlines():
        a, b, c, x, *d, = re.split('[ :-]', line.strip())
        data.append(list(zip(a, b, c, d)))

print([0][2])