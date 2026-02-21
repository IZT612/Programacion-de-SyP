from classes import VocalCounterThread
import os

def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'fichero.txt'), "r", encoding="utf-8") as f:
            contenido = f.read()
    except FileNotFoundError:
        contenido = "Este es un texto de prueba para contar vocales concurrentemente."
        print("No se encontró texto.txt, usando frase de prueba...")

    vocales = ['a', 'e', 'i', 'o', 'u']
    hilos = []

    print(f"Analizando texto de longitud: {len(contenido)} caracteres.\n")

    for v in vocales:
        hilo = VocalCounterThread(v, contenido)
        hilos.append(hilo)
        hilo.start()

    for h in hilos:
        h.join()

    print("\nConteo finalizado.")

if __name__ == "__main__":
    main()