import sys

filename = open(sys.argv[1])
fileContent = filename.readlines()
filename.close()

for line in fileContent:
    line = line.strip('\n')
    l1, l2 = [list(x) for x in line.split(';')]
    grid = []
    for x in range(len(l1)+1):
        grid.append([0 for s in range(len(l2)+1)])
    for y in range(len(l2)):
        for x in range(len(l1)):
            if l1[x] == l2[y]:
                grid[x+1][y+1] = grid[x][y] + 1
            else:
                grid[x+1][y+1] = max(grid[x+1][y], grid[x][y+1])
    pos = [len(grid) - 1, len(grid[len(grid)-1])-1]
    cur = None
    subseq = []
    while cur != 0:
        cur = grid[pos[0]][pos[1]]
        if (grid[pos[0]-1][pos[1]] != cur and
                grid[pos[0]][pos[1]-1] != cur):
            subseq.append(l1[pos[0]-1])
            pos[0] -= 1
            pos[1] -= 1
        elif grid[pos[0]-1][pos[1]] == cur:
            pos[0] -= 1
        else:
            pos[1] -= 1
    print(''.join(reversed(subseq)))
