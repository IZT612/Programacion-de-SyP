lista = []

contador = 8

while contador != 0:

    lista.append(int(input("Introduzca un número entero.")))

    contador -= 1

for numero in lista:

    tipo = "par" if numero % 2 == 0 else "impar"

    print(str(numero), tipo)