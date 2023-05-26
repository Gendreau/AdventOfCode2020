card = 17115212
door = 3667832

def find_loop_size(public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value *= 7
        value %= 20201227
        loop_size += 1
    return(loop_size)

def find_encryption_key(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227
    return(value)

card_loop_size = find_loop_size(card)
print(find_encryption_key(door, card_loop_size))