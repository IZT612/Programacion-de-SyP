numbers = []

result = 0

number_input = int(input("Type a number: "))

while (number_input >= 0):
    
    numbers.append(number_input)

    number_input = int(input("Type another number: "))

for number in numbers:
    
    result += number

print("The total sum is", result)