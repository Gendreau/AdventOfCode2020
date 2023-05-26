contains_me, inside_me = {}, {}
for line in open('./inputs/7.txt').read().split('\n'):
    a, b = line.split(' bags contain ')
    b = b.split(', ')
    for bag in b:
        bag = bag.split(' bag')
        if bag[0][0].isnumeric():
            if bag[0][2:] not in contains_me:
                contains_me[bag[0][2:]] = [a]
            else:
                contains_me[bag[0][2:]].append(a)
            if a not in inside_me:
                inside_me[a] = [[int(bag[0][0]), bag[0][2:]]]
            else:
                inside_me[a].append([int(bag[0][0]), bag[0][2:]])

def count_contains(color, containers):
    for bag in contains_me[color]:
        containers.add(bag)
        if bag in contains_me: containers = count_contains(bag, containers)
    return containers

def count_inside(color):
    total = 0
    for bag in inside_me[color]:
        total += bag[0] * count_inside(bag[1]) + bag[0] if bag[1] in inside_me else bag[0]
    return total

print(len(count_contains('shiny gold', set())))
print(count_inside('shiny gold'))