# Exercise 4:
# Develop a program called Lab4Exc4 to achieve the following operations:
# • Read n integers from keyboard.
# • Display the min and max values entered.
# • The program ends when -1 is entered.
def Lab4Exc4():
    n = int(input("Enter n: "))
    numbers = []
    while True:
        num = int(input("Enter an integer (-1 to exit): "))
        if num == -1:
            break
        numbers.append(num)

    if numbers:
        min_value = min(numbers)
        max_value = max(numbers)
        print("Min value:", min_value)
        print("Max value:", max_value)
    else:
        print("No numbers entered.")


Lab4Exc4()
