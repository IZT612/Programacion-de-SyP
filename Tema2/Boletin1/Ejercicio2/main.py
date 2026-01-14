from funcion import sumarNumeros
from multiprocessing import Process, Pool
import os
import time

if __name__ == "__main__":

    cantidad_procesos = int(input("Introduzca cuantos procesos quiere hacer: "))

    contador = 0

    numeros = []

    while(contador < cantidad_procesos):

        contador += 1

        numero = int(input("Introduzca un número para sumar todos los números desde el 1 hasta el que introduzca: "))

        numeros.append(numero)

    with Pool(processes=4) as pool:

        inicio = time.perf_counter()
        results = pool.map(sumarNumeros, numeros)
        fin = time.perf_counter()

        tiempo_pool = fin - inicio

        print("Todos los procesos han terminado en", tiempo_pool, "segundos")
