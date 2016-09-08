import sys
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = line.strip('\n')
    line = line.strip(';')
    line = [(x.split(',')) for x in line.split('; ')]
    cities = {key: int(value) for (key, value) in line}
    distances = sorted([(x) for x in cities.values()])
    output = [distances[0]]
    for i in range(1, len(distances)):
        output.append(distances[i] - distances[i-1])
    print(','.join(map(str, output)))
