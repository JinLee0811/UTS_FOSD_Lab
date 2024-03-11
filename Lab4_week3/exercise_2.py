# Develop a program called Lab4Exc2 to achieve the following operations:
# • Generate 20 random integers
# • Store the values into an array
# • Display the array


import random


def Lab4Exc2():
    arr = []
    for i in range(20):
        arr.append(random.randint(0, 100))
    print(arr)


Lab4Exc2()
