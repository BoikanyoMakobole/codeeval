import sys


def plus(p1, p2):
    return p1 + p2


def minus(p1, p2):
    return p1 - p2

operations = {'-': minus, '+': plus}
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = line.strip('\n')
    nums, seq = [list(x) for x in line.split()]
    seq = [x - 97 for x in list(map(ord, seq))]  # -52 = -, -54 = +
    p1 = []
    p2 = []
    current = p1
    operation = None
    for item in seq:
        if item == -52 or item == -54:
            current = p2
            if item == -52:
                operation = '-'
            else:
                operation = '+'
        else:
            current.append(nums[item])
    c1 = int(''.join(p1))
    c2 = int(''.join(p2))
    print(operations[operation](c1, c2))
