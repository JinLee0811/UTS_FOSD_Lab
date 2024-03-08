# 1. Please enter the x1 coordinate of point A: 1.0
# 2. Please enter the y1 coordinate of point A: 2.0
# 3. Please enter the x2 coordinate of point B: 3.0
# 4. Please enter the y2 coordinate of point B: 4.0
# 5. The distance between A(x1,y1) and B(x2,y2) is distance
# A = x,y
# B = x2,y2

# 두 점사이의 거리는 x2 - x1 과 y2 - y1 을 곱하고 제곱근을 구한다.
# 피타고라스의 성질을 이용하자


import math

x1 = float(input("Please enter the x1 coordinate of point A: "))
y1 = float(input("Please enter the y1 coordinate of point A: "))
x2 = float(input("Please enter the x2 coordinate of point B: "))
y2 = float(input("Please enter the y2 coordinate of point B: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(
    f"The distance between A({x1:.2f}, {y1:.2f}) and B({x2:.2f}, {y2:.2f}) is {distance:.2f}"
)
