# q = True if (5 % 2 != 0) else False
# print(q)

# a = True
# b = True

# C = a and b or True
# print(C)

# sum = 0
# # adds values from 1 to 19 to sum
# for e in range(1, 20):
#     sum += e

# print("Sum = ", sum)

import sys

rain = int(input("rain : "))
count = 0
maximum = -sys.maxsize

while rain != -1:
    if rain == 0:
        count += 1
    else:
        maximum = max(maximum, count)
        count = 0
    rain = int(input("rain : "))
maximum = max(maximum, count)

print(maximum)
