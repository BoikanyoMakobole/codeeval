import sys
import re
import math
regex = re.compile('-?\d+')
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = line.strip('\n')
    x1, y1, x2, y2 = list(map(float, regex.findall(line)))
    distance = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
    print(int(distance))
