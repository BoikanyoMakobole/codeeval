#!python3

import sys

file = open(sys.argv[1])
fileContent = file.readlines()
words = []
for item in fileContent:
    item = item[:-1]
    words.append(item)
num_of_items = int(words[0])
words.pop(0)
for i in range(0, num_of_items):
    king_of_hill = words[0]
    for word in words:
        if len(word) > len(king_of_hill):
            king_of_hill = word
    print(king_of_hill)
    words.remove(king_of_hill)
