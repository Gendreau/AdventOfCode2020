with open('./inputs/10.txt') as f:
    adapters = [int (x) for x in list(filter(None, f.read().split("\n")))]
isPartOne = False

adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()
differences = [0, 0, 0]
tribonacci = [1,1,2]

def get_trib(n):
    if n < len(tribonacci): return tribonacci[n]
    tmp = get_trib(n-1) + get_trib(n-2) + get_trib(n-3)
    tribonacci.append(tmp)
    return tmp

if isPartOne:
    for i in range(1, len(adapters)):
        differences[adapters[i]-adapters[i-1]-1] += 1
    print(differences[0] * differences[2])
else:
    total = 1
    run = 0
    for i in range(1, len(adapters)):
        if adapters[i]-adapters[i-1] == 1:
            run += 1
        else:
            total *= get_trib(run)
            run = 0
    print(total)