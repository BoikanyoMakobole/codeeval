import sys
filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = line.strip('\n')
    seq = line.split(',')
    nums = []
    words = []
    for item in seq:
        try:
            nums.append(int(item))
        except ValueError:
            words.append(item)
    if not words:
        print(','.join(map(str, nums)))
    elif not nums:
        print(','.join(words))
    else:
        print('|'.join([','.join(x) for x in [words, list(map(str, nums))]]))
