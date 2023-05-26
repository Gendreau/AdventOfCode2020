import itertools

with open('./inputs/9.txt') as f:
    numbers = [int (x) for x in list(filter(None, f.read().split("\n")))]
preamble = 25

for i in range(preamble, len(numbers)):
    stored = numbers[i-preamble:i]
    valid = [numbers[i] for a, b in itertools.combinations(stored, 2) if a + b == numbers[i]]
    if not valid: 
        invalid = numbers[i]
        index = i
        break
print("Invalid number:", invalid)

for i in range(3,index):
    for j in range(i, len(numbers)):
        if sum(numbers[j-i:j]) == invalid:
            print("Encryption weakness:", min(numbers[j-i:j])+max(numbers[j-i:j]))
            break