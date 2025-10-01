lista = []

contador = 10

while contador != 0:

    lista.append(int(input("Introduce un número.")))

    contador -= 1

lista.sort(reverse=True)

print(lista)
