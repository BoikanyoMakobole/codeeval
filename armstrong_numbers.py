import sys
import math
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = int(line.strip('\n'))
    nums = [math.pow(int(i), len(str(line))) for i in str(line)]
    if sum(nums) == line:
        print(True)
    else:
        print(False)
