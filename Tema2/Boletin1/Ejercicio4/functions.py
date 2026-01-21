import os

def leerFichero(conn):
    ruta = os.path.join(os.path.dirname(__file__), "archivo.txt")

    with open(ruta, "r") as archivo:
        for linea in archivo:
            conn.send(int(linea.strip()))

    conn.send(None)
    conn.close()

def sumarNumeros(conn):
    resultado = 0

    while True:
        numero = conn.recv()

        if numero is None:
            break

        resultado += numero

    conn.close()
    print("Resultado:", resultado)