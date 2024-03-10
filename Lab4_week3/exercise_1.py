# Develop a program called Lab4Exc1 to achieve the following operations:
# • Display all numbers from 1 to 10
# • Display the square roots of each number
# • Display the exponents of each number
# • Show all displays in a tabular format (refer to lecture 4)

# i , i 의 2분의 1제곱 , exponents 거듭제곱


def Lab4Exc1():
    print("Numbers\tSquare Root\tExponent")
    for i in range(1, 11):
        print(i, "\t", i**0.5, "\t", i**2)


Lab4Exc1()
