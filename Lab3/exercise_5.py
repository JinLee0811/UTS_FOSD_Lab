# 1. Please enter a string: type your input here
# 2. First character: display first character of the string
# 3. Last character: display last character of the string
# 4. Lower-case string: convert and display the string in lower-case
# 5. String length: display the length of the string


stringInput = str(input("Please enter a string:"))
FirstCharacter = stringInput[0]
LastCharacter = stringInput[-1]
LowerCaseString = stringInput.lower()
StringLength = len(stringInput)


print(f"First character: {FirstCharacter}")
print(f"Last character: {LastCharacter}")
print(f"Lower-case string: {LowerCaseString}")
print(f"String length: {StringLength}")
