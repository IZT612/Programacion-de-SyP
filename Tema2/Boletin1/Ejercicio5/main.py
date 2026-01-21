from function import sumarNumeros
from multiprocessing import Process
import os
import time

if __name__ == "__main__":

    cantidad_procesos = int(input("Introduzca cuantos procesos quiere hacer: "))

    contador = 0

    procesos = []

    while(contador < cantidad_procesos):

        contador += 1

        numero_inicial = int(input("Introduzca un número desde el que empezar a sumar: "))

        numero_limite = int(input("Introduzca un número para hasta el que sumar: "))

        procesos.append(Process(target=sumarNumeros, args=(numero_inicial, numero_limite)))

    inicio_total = time.perf_counter()

    for p in procesos:

        inicio = time.perf_counter()
        p.start()
        p.join()
        fin = time.perf_counter()

        tiempo_proceso = (fin - inicio)

        print("El proceso ha acabado en", tiempo_proceso, "segundos")

    fin_total = time.perf_counter()

    tiempo_total = fin_total - inicio_total

    print("Todos los procesos han tardado en total", tiempo_total, "segundos")