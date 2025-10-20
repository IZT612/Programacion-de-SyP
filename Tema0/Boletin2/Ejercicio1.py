import random

# Contador, para saber cuantas veces añadiremos un numero
contador = 10

# Creamos la lista
lista = []

# Mientras el contador no sea 0, seguirá el bucle
while contador != 0:

    # Añadimos a la lista un numero aleatorio entre 1 y 101
    lista.append(random.randint(1,101))

    # Reducimos el contador
    contador -= 1


# La vemos
print(lista)