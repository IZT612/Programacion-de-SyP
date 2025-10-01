lista = []

contador = 10

while contador != 0:

    numero_usuario = int(input("Introduzca un número."))

    lista.append(numero_usuario)

    contador -= 1

minimo = lista[0]

maximo = lista[0]

for numero in lista:

    if (numero < minimo):

        minimo = numero
    
    if (numero > maximo):

        maximo = numero

print("El mínimo de la lista es:", minimo, ", mientras que el máximo es", maximo)