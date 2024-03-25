import validator as v


class Person:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        return self.name, self.email, self.password

    def validEmail(self):
        return v.validator.validEmail(self.email)

    def validPassword(self):
        return v.validator.validPassword(self.password)


p = Person(input("Name: "), input("Email: "), input("Password: "))

if not (p.validEmail()):
    print("Invalid email")
elif not (p.validPassword()):
    print("Invalid password")
else:
    if p.login():
        print(f"Welcome {p.name}")
    else:
        print("Login failed")
