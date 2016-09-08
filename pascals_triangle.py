import sys

filename = open(sys.argv[1])
fileContent = filename.readlines()
filename.close()

for line in fileContent:
    output = []
    depth = int(line)
    for n in range(depth):
        result = []
        for k in range(n+1):
            if k == 0:
                num = 1
            else:
                try:
                    num = output[n-1][k-1] + output[n-1][k]
                except IndexError:
                    num = 1
            result.append(num)
        output.append(result)
    print(' '.join(map(str, [x for item in output for x in item])))
