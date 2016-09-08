import sys

zero = """-**--
*--*-
*--*-
*--*-
-**--
-----"""
one = """--*--
-**--
--*--
--*--
-***-
-----"""
two = """***--
---*-
-**--
*----
****-
-----"""
three ="""***--
---*-
-**--
---*-
***--
-----"""
four = """-*---
*--*-
****-
---*-
---*-
-----"""
five = """****-
*----
***--
---*-
***--
-----"""
six = """-**--
*----
***--
*--*-
-**--
-----"""
seven = """****-
---*-
--*--
-*---
-*---
-----"""
eight = """-**--
*--*-
-**--
*--*-
-**--
-----"""
nine ="""-**--
*--*-
-***-
---*-
-**--
-----"""

codes = [zero, one, two, three, four, five, six, seven, eight, nine]
ciph = []
for item in codes:
    ciph.append(item.split('\n'))

filename = open(sys.argv[1])
fileContent = filename.readlines()
for line in fileContent:
    line = list(line.strip('\n'))
    p1 = []
    for item in line:
        if item.isdigit():
            p1.append(int(item))
    seq = []
    for item in p1:
        seq.append(ciph[item])

    for q in range(6):
        for i in range(0, len(seq)):
            sys.stdout.write(seq[i][q])
        print('')
