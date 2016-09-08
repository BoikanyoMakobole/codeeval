import sys


def happy(num, tried):
    sequence = [int(i) for i in str(num)]
    sqrs = []
    for item in sequence:
        sqrs.append(item*item)
    sums = sum(sqrs)
    if sums == 1:
        return 1
    elif sums in tried:
        return 0
    else:
            tried.append(sums)
            return happy(sums, tried)


filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = int(line)
    tried = []
    print(happy(line, tried))
