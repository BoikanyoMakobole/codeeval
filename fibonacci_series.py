import sys
import math


def binet(n):
    return (((math.pow((1+math.sqrt(5)), n)) - (math.pow((1-math.sqrt(5)), n)))/((math.pow(2, n))*(math.sqrt(5))))

filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    n = float(line)
    print(int(binet(n)))
