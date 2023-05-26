import re
import sys
import copy
import numpy

commands = []
with open('./inputs/8.txt') as f:
    for line in f.readlines():
        a, b = re.split(' ', line.strip())
        c = b[1:]
        b = 1 if b[0] == '+' else -1
        commands.append(list((a, b, int(c))))

def run(commands):
    acc = 0
    reg = 0
    executed = numpy.zeros(len(commands), dtype=int)
    while executed[reg] == 0:
        executed[reg] = 1
        if commands[reg][0] == 'jmp':
            reg += commands[reg][1] * commands[reg][2] - 1
        elif commands[reg][0] == 'acc':
            acc += commands[reg][1] * commands[reg][2]
        reg += 1
        if reg == len(commands):
            print(acc)
            return
    return acc

print(run(commands))

for i in range(len(commands)):
    s_commands = copy.deepcopy(commands)
    if s_commands[i][0] == 'acc' or s_commands[i][2] == 0: continue
    else: s_commands[i][0] = 'nop' if s_commands[i][0] == 'jmp' else 'jmp'
    run(s_commands)