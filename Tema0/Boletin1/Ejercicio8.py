size = int(input("Type the number that indicates the base and height of the triangle: "))

for layer in range(1, (size + 1)):
    line = " " * (size - layer) 
    line += "* " * layer
    print(line)