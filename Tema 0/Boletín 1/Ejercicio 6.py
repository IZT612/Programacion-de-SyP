number = int(input("Type a number to get its factorial: "))

result = 1

multiplier = 1

while multiplier <= number:

    result *= multiplier

    multiplier += 1

print("The factorial of", number, "is", result)