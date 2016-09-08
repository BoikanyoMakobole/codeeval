import sys

filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    nums, p1, p2 = list(map(int, line.split(',')))
    n = bin(nums)[2:]
    maximus = max(p1, p2)
    if maximus > len(n):
        n = '0' * maximus + n
    if n[-p2] == n[-p1]:
        print('true')
    else:
        print('false')
