import sys

filename = open(sys.argv[1])
fileContent = filename.readlines()
filename.close()

for line in fileContent:
    line = list(line.strip('\n'))
    output = []
    for i in range(0, len(line)-1):
        if line[i] != line[i+1]:
            output.append(line[i])
    output.append(line[-1])
    print(''.join(output))
