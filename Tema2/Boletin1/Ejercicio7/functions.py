import os

def sumarNumeros(cola):
    while True:
        tupla = cola.get()

        if tupla is None:
            break

        num1, num2 = tupla

        if num1 > num2:
            mayor = num1
            menor = num2
        else:
            mayor = num2
            menor = num1

        resultado = 0

        contador = menor
        while contador <= mayor:
            resultado += contador
            contador += 1

        print(resultado)


def leerFichero(cola):

    ruta = os.path.join(os.path.dirname(__file__), "archivo.txt")

    with open(ruta, "r") as archivo:
        for linea in archivo:
            num1, num2 = map(int, linea.split())
            cola.put((num1, num2))

    cola.put(None)
