import os

def sumarNumeros(conn):
    while True:
        tupla = conn.recv()

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

    conn.close()


def leerFichero(conn):

    ruta = os.path.join(os.path.dirname(__file__), "archivo.txt")

    with open(ruta, "r") as archivo:
        for linea in archivo:
            num1, num2 = map(int, linea.split())
            conn.send((num1, num2))

    conn.send(None)
    conn.close()
