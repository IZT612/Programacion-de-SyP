import os

def leerFichero(cola):

    ruta = os.path.join(os.path.dirname(__file__), "archivo.txt")

    with open(ruta, "r") as archivo:
        for linea in archivo:
            numero = int(linea.strip())
            cola.put(numero)

    cola.put(None)

def sumarNumeros(cola):

    resultado = 0

    while True:

        numero = cola.get()

        if numero is None:

            break

        resultado += numero

    print('Resultado', resultado)
    
