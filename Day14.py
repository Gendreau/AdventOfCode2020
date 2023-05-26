import copy

lines = [x for x in open('./inputs/14.txt').read().strip().split('\n')]

class Instruction:
    def __init__(self, mask):
        self.mask = mask
        self.writes = []
    
    def add(self, address, value):
        self.writes.append([address, value])
    
    def get_mask(self):
        return self.mask

    def get_writes(self):
        return self.writes

masks, index = [], -1
for line in lines:
    line = line.split(' = ')
    if line[0] == 'mask':
        masks.append(Instruction(line[1]))
        index += 1
    else:
        masks[index].add(int(line[0][4:-1]), int(line[1]))

def apply_mask(mask, value):
    filler = '000000000000000000000000000000000000'
    value = str(bin(value)[2:])
    applied = ''
    if len(value) < 36:
        value = filler[:36-len(value)] + value
    for i in range(36):
        applied += mask[i] if mask[i] != 'X' else value[i]
    return int(applied,2)

def apply_address_mask(mask, address):
    filler = '000000000000000000000000000000000000'
    address = str(bin(address)[2:])
    applied = ['']
    if len(address) < 36:
        address = filler[:36-len(address)] + address
    for i in range(36):
        if mask[i] == '0':
            for j in range(len(applied)): applied[j] += address[i]
        elif mask[i] == '1':
            for j in range(len(applied)): applied[j] += '1'
        elif mask[i] == 'X':
            sublist = applied.copy()
            for j in range(len(applied)): applied[j] += '0'
            for j in range(len(sublist)): sublist[j] += '1'
            applied += sublist
    return applied

memory = {}
for maskg in masks:
    for write in maskg.get_writes():
        memory[write[0]] = apply_mask(maskg.get_mask(), write[1])
print(sum(memory.values()))

memory = {}
for maskg in masks:
    for write in maskg.get_writes():
        addresses = apply_address_mask(maskg.get_mask(), write[0])
        for address in addresses:
            memory[int(address,2)] = write[1]
print(sum(memory.values()))