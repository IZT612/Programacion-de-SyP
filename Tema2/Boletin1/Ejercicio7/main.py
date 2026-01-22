from functions import sumarNumeros, leerFichero
from multiprocessing import Process, Queue
import time

if __name__ == "__main__":

    cola = Queue()

    p1 = Process(target=leerFichero, args=(cola,))
    p2 = Process(target=sumarNumeros, args=(cola,))

    inicio = time.perf_counter()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    fin = time.perf_counter()

    tiempo_total = fin - inicio

    print("Todos los procesos han terminado en", tiempo_total, "segundos")
