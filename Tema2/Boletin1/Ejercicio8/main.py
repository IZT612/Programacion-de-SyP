from functions import sumarNumeros, leerFichero
from multiprocessing import Process, Pipe
import time

if __name__ == "__main__":

    conn_sumar, conn_leer = Pipe()

    p1 = Process(target=leerFichero, args=(conn_leer,))
    p2 = Process(target=sumarNumeros, args=(conn_sumar,))

    inicio = time.perf_counter()

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    fin = time.perf_counter()

    tiempo_total = fin - inicio

    print("Todos los procesos han terminado en", tiempo_total, "segundos")
