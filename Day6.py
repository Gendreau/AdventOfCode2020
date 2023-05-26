import functools
print(sum(len(''.join(set(x.replace('\n','')))) for x in open('./inputs/6.txt').read().split("\n\n")))
print(sum(len(functools.reduce(set.intersection, [set(item) for item in x])) for x in [x.split('\n') for x in open('./inputs/6.txt').read().split("\n\n")]))