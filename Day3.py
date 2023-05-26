forest = [l.rstrip('\n') for l in open('./inputs/3.txt')]

def traverse(right, down):
    trees, x, y = 0, 0, 0
    while y < len(forest)-down:
        x = (x+right)%len(forest[y])
        y += down
        trees += 1 if forest[y][x] == '#' else 0
    return trees

print(traverse(3,1))

slopes, product = [[1,1],[3,1],[5,1],[7,1],[1,2]], 1
for slope in slopes:
    product *= traverse(slope[0],slope[1])
print(product)