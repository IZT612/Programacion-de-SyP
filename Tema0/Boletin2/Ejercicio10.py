diccionario = {'e': 'p', 'i': 'v', 'k': 'i', 'm': 'u', 'p': 'm', 'q': 't', 'r': 'e', 's': 'r', 't': 'k', 'u': 'q', 'v': 's'}

frase_usuario = input('Introduce una palabra para encriptarla: ')

frase_encriptada = ''

encontrar_letra = ''

for letra in frase_usuario:
    
    encontrar_letra = diccionario.get(letra)

    if encontrar_letra != None:

        frase_encriptada += encontrar_letra

    else:

        frase_encriptada += letra

    encontrar_letra = None

print('La frase encriptada es la siguiente:\n', frase_encriptada)