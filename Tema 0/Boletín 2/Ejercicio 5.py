import random

lista = []

contador = 100

veces = 0

while contador != 0:

    lista.append(random.randint(1, 11))

    contador -= 1

numero_buscar = int(input("Introduce un número a buscar: "))

print(lista)

print("El número aparece", lista.count(numero_buscar), "veces.")