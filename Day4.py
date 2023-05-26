import re

with open('./inputs/4.txt') as f:
    passports = [x for x in f.read().strip().split('\n\n')]
PartOne = False
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def get_field(passport, field):
    return passport[passport.index(field)+1]

if PartOne:
    print(sum(1 for passport in passports if all(field in passport for field in fields)))
else:
    valids = 0
    for passport in passports:
        if (all(field in passport for field in fields)):
            p = re.split('[\n :]', passport)
            if (
                1920 <= int(get_field(p, 'byr')) <= 2002 
                and 2010 <= int(get_field(p, 'iyr')) <= 2020
                and 2020 <= int(get_field(p, 'eyr')) <= 2030
                and (get_field(p,'hgt')[2:4] == 'in' and 59 <= int(get_field(p,'hgt')[:2]) <= 76
                    or (get_field(p,'hgt')[3:5]) == 'cm' and 150 <= int(get_field(p, 'hgt')[:3]) <= 193)
                and re.match('#[0-9a-f]{6}',get_field(p,'hcl'))
                and get_field(p,'ecl') in eyecolors
                and (re.match('\d{9}', get_field(p,'pid')) and len(get_field(p, 'pid')) == 9)
            ):
                valids += 1
print(valids)