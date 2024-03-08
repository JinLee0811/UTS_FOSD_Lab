# 1- The class should have two fields: make and pos
# 2- Define a constructor that initializes the fields
# 3- Define a function to move the position by distance
# 4- Define the object descriptive function that returns: <make> is at position <pos value>
# 5- Create an object car of Type Car and initialize it to “BMW” and 0
# 6- Print current position
# 7- Move the car by 15
# 8- Print the new position


# 거리에 따른 위치 변화
# 0에서 이동한 거리 + 해주기


class car:
    def __init__(self, make, pos):
        self.make = make
        self.pos = pos

    def move(self, distance):
        self.pos += distance

    def __str__(self):  # 객체를 문자열로 사용하여 함수 내부에서 사용
        return f"{self.make} is at position {self.pos}"


Car = car("BMW", 0)
Car.move(15)
print(Car)
