matrix = []
for y in range(1, 13):
    matrix.append([(y*x) for x in range(1, 13)])

ciph = "{:>4}"*12
for i in range(0, 12):
    print(ciph.format(*matrix[i]).lstrip())
