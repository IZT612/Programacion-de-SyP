import os
from multiprocessing import Process

def contar_vocal(vocal, fichero):
    contador = 0
    # Usamos os.path.join para construir la ruta del archivo de forma segura
    ruta = os.path.join(os.path.dirname(__file__), fichero)
    
    # Abrimos el fichero en modo lectura
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            contador += linea.lower().count(vocal)  # Contamos la vocal sin distinguir mayúsculas y minúsculas
    
    print(f"La vocal '{vocal}' aparece {contador} veces en el archivo {fichero}")

if __name__ == "__main__":
    fichero = "fichero.txt"  # Nombre del archivo, aseguramos que esté en la misma carpeta
    vocales = ["a", "e", "i", "o", "u"]

    procesos = []

    for vocal in vocales:
        p = Process(target=contar_vocal, args=(vocal, fichero))
        procesos.append(p)
        p.start()  # Iniciamos cada proceso

    for p in procesos:
        p.join()  # Esperamos que todos los procesos terminen
