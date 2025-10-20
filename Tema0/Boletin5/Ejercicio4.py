fichero_desordenado = open('Tema 0/Boletín 5/ficheros/Ejercicio_4f_desordenado.txt', 'rt')

numeros = []

for numero in fichero_desordenado.readlines():

    numero = numero.split('\n')[0]

    numeros.append(int(numero))

fichero_desordenado.close()

numeros.sort()

fichero_ordenado = open('Tema 0/Boletín 5/ficheros/Ejercicio_4f_ordenado.txt', 'w', encoding='utf8')

for numero in numeros:

    fichero_ordenado.write(str(numero) + '\n')