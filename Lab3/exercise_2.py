# 1. Read in the integer values of x and y from STDIN
# 2. declare a variable z assign the result of x power y to it power = 제곱
# 3. declare a variable called ‘result’ and assign the square-root of z to it
# 4. print out each of the above results on a new line (formatted at 2 decimal points)


import math

x = int(input("x = "))
y = int(input("y = "))
z = x**y
result = math.sqrt(z)

print(f"x: {x:.2f}")
print(f"y: {y:.2f}")
print(f"z: {z:.2f}")
print(f"result: {result:.2f}")
