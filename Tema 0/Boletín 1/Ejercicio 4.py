import random

secret_number = random.randint(1, 101)

print("Try to guess the secret number!")

number_input = int(input("Type a number: "))

while (number_input != secret_number):

    if (number_input > secret_number):
        
        print(number_input, "is higher than the secret number.")
    else:
        print(number_input, "is lower than the secret number.")

    number_input = int(input("Type another number."))

print("Good job, the secret number was", secret_number)