import sys

filename = open(sys.argv[1])
fileContent = filename.readlines()
filename.close()
for line in fileContent:
    line = line.strip('\n')
    l = 0.0
    u = 0.0
    for item in line:
        if item.islower():
            l += 1.0
        else:
            u += 1.0
    l = l/len(line)*100
    u = u/len(line)*100
    print("lowercase: {:.2f} uppercase: {:.2f}".format(l, u))
