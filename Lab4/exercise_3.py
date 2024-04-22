def Lab4Exc3():
    i = int(input("Enter a number: "))
    if i != 0:
        for i in range(1, i + 1):
            star = "*"
            print(star * i)
    elif i == 0:
        return print("Good bye")


Lab4Exc3()
