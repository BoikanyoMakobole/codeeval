import sys

filename = open(sys.argv[1])
fileContent = filename.readlines()
filename.close()


def palindrome(start, count):
    s1 = int(start)
    s2 = int(start[::-1])
    if s1 != s2:
        count += 1
        return palindrome(str(s1+s2), count)
    else:
        return s1, count

for line in fileContent:
    line = line.strip('\n')
    s1, count = palindrome(line, 0)
    print(str(count) + ' ' + str(s1))
