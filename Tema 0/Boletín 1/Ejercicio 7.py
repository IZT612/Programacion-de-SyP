number = int(input("Type a poitive number to see if its a prime number: "))

divisor = 2

prime = True

while prime and divisor <= (number / 2):

    if number % divisor == 0:

        prime = False

    divisor += 1

result = "is" if prime else "isn't"

print("The number", result, "prime.")

        