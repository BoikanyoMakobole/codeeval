import sys
import re

regex = re.compile(r'(0+)\s(0+)')

filename = open(sys.argv[1])
fileContent = filename.readlines()
filename.close()
for line in fileContent:
    line = line.strip('\n')
    mo = regex.findall(line)
    output = []
    for item in mo:
        c = '0'
        if item[0] == '00':
            c = '1'
        else:
            pass
        for x in range(len(item[1])):
            output.append(c)
    binary = ''.join(output)
    print(int(binary, 2))
