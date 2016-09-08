import sys
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    nums = list(map(int, line.split()))
    winners = []
    for i in range(10):
        if nums.count(i) == 1:
            winners.append(i)
    winners = sorted(winners)
    if not winners:
        print(0)
    else:
        winner = winners[0]
        print(nums.index(winner) + 1)
