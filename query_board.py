import sys


def SetRow(i, x, matrix):
    """All Values in row i will be changed to x"""
    for s in range(256):
        matrix[i][s] = x
    return matrix


def SetCol(j, x, matrix):
    """All values in column j will be changed to x"""
    for s in range(256):
        matrix[s][j] = x
    return matrix


def QueryRow(i, matrix):
    """Output the sum of row i"""
    print(sum(matrix[i]))
    return matrix


def QueryCol(j, matrix):
    """Output the sum of column j"""
    output = 0
    for s in range(256):
        output += matrix[s][j]
    print(output)
    return matrix

functions = {
    'SetRow': SetRow,
    'SetCol': SetCol,
    'QueryRow': QueryRow,
    'QueryCol': QueryCol}
matrix = [[0 for x in range(256)] for x in range(256)]
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = line.strip('\n')
    command = line.split()
    if len(command) == 3:
        matrix = functions[command[0]](
            int(command[1]), int(command[2]), matrix)
    else:
        matrix = functions[command[0]](int(command[1]), matrix)
