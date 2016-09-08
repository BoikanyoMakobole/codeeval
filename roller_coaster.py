import sys

filename = open(sys.argv[1])
fileContent = filename.readlines()
filename.close()
for line in fileContent:
    line = line.strip('\n')
    current = True
    output = []
    for item in list(line):
        if item.isalpha():
            if current:
                output.append(item.upper())
                current = False
            else:
                output.append(item.lower())
                current = True
        else:
            output.append(item)
    print(''.join(output))
