cadena = input("Introduzca una cadena de texto.")

palabras = cadena.split()

diccionario = {}

for palabra in palabras:

    if diccionario.get(palabra) == None:

        diccionario[palabra] = 1

    else:

        diccionario[palabra] += 1

print(diccionario)