from functions import sumarNumeros
from multiprocessing import Pool
import time

if __name__ == "__main__":

    cantidad_procesos = int(input("Introduzca cuantos procesos quiere hacer: "))

    contador = 0

    numeros1 = []
    numeros2 = []

    while(contador < cantidad_procesos):

        contador += 1

        numero1 = int(input("Introduzca un número: "))

        numero2 = int(input("Introduzca otro número para sumar los que hay entre este y el anterior: "))

        numeros1.append(numero1)

        numeros2.append(numero2)

    with Pool(processes=4) as pool:

        inicio = time.perf_counter()
        pool.starmap(sumarNumeros, zip(numeros1, numeros2))
        fin = time.perf_counter()

        tiempo_pool = fin - inicio

        print("Todos los procesos han terminado en", tiempo_pool, "segundos")
