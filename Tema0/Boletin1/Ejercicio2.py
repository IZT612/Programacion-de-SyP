num1 = int(input("Type a number: "))
num2 = int(input("Type another number: "))

if (num1 < num2):
    print(num1, "<", num2)
elif (num2 < num1):
    print(num2, "<", num1)
else:
    print(num1, "=", num2)
    