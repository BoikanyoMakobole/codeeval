import sys
import re
regex = re.compile(r"(.+?)\1+")
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = line.strip('\n')
    matches = None
    for match in regex.finditer(line):
        matches = match.group(1)
    if matches:
        print(len(matches))
    else:
        print(len(line))
