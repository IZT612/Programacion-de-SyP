def maximum(number1, number2):

    result = number1 if number1 > number2 else number2
    
    return result

number1 = int(input("Type a number: "))
number2 = int(input("Type another number: "))

result = maximum(number1, number2)

print(result, "is higher.")