# 1- Create an array of integers called ‘numbers’ of size n
# 2- read n from STDIN
# 3- Display the array
# 4- Modify the first element to 10
# 5- Modify the last element to -5
# 6- Modify the middle element to 3
# 7- Display the array again


# 1- Create an array of integers called ‘numbers’ of size n
# 2- read n from STDIN
n = int(input("Enter the size of the array: "))
numbers = [0] * n

# 3- Display the array
print("Initial array:", numbers)

# 4- Modify the first element to 10
numbers[0] = 10

# 5- Modify the last element to -5
numbers[-1] = -5

# 6- Modify the middle element to 3
if n % 2 == 0:
    # if the array size is even, there's no single middle element
    middle_index = n // 2 - 1
else:
    middle_index = n // 2

numbers[middle_index] = 3

# 7- Display the array again
print("Modified array:", numbers)


# import numpy as np

# class Numbers:
#     def __init__(self):
#         pass

#     def main():
#         print("n = ", end="")
#         n = int(input())
#         numbers = np.zeros(n, dtype=int)
#         print(numbers)
#         numbers[0] = 10
#         numbers[-1] = -5
#         numbers[n // 2] = 3
#         print(numbers)

# if __name__ == "__main__":
#     Numbers.main()
