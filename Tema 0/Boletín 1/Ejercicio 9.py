def count(number1, number2):

    numbers = []

    range2 = range(number1, number2) if number1 < number2 else range(number2, number1)

    for number in range2:

        numbers.append(number)

    return numbers

number1 = int(input("Type the first number: "))
number2 = int(input("Type the second number: "))

numbers = count(number1, number2)

for number in numbers:

    print(number)