import random

givno = int(input("Please, input the number of numbers: "))
fix = 1

while fix <= givno:
    print("#%06x" % random.randint(0, 0xFFFFFF))
    fix += 1