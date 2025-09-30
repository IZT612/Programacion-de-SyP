
# Lista de vocales
vocales = ('a', 'e', 'i', 'o', 'u')

# Funcion que verifica si la letra que recibe por parametro es vocal
def es_vocal_fnct(letra) :

    # Booleano que indica si es vocal
    es_vocal = False

    # Recorremos las letras en la lista de vocales
    for vocal in vocales:

        # Si la letra coincide con alguna
        if letra == vocal:

            # Es vocal
            es_vocal = True

    # Devolvemos el boolean
    return es_vocal

# Probamos

print(str(es_vocal_fnct('b')))

print(str(es_vocal_fnct('a')))