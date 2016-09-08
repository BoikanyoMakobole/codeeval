import sys
import re
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = line.strip('\n')
    regex = re.compile('[^a-zA-Z]')
    line = regex.sub('', line)
    line = line.replace(' ', '')
    chrs = list(line.lower())
    counts = {}
    for item in chrs:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    points = 26
    score = 0
    while counts:
        king = max(counts, key=counts.get)
        score += counts[king] * points
        points -= 1
        del counts[king]
    print(score)
