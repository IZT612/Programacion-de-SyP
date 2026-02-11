import multiprocessing
import os
from functions import generar_temperaturas, buscar_maxima, buscar_minima, CARPETA

if __name__ == "__main__":
    
    # Mes en el que registraremos las temperaturas (El ejercicio pide específicamente diciembre)
    mes = 12

    # Argumentos que recibirá cada proceso, el día (del 1 al 31) y mes
    argumentos = [(dia, mes) for dia in range(1, 32)]

    print("--- FASE 1: Generación de ficheros con Pool ---")
    
    # Creamos la Pool para el primer proceso
    with multiprocessing.Pool() as pool:

        # Generamos las temperaturas para cada día del mes
        pool.starmap(generar_temperaturas, argumentos)
        
    print("Fase 1 completada.\n")

    print("--- FASE 2: Cálculo de Máximas y Mínimas ---")

    # Creamos la Pool para los dos últimos procesos
    with multiprocessing.Pool() as pool:

        # Guardamos las temperaturas máximas y mínimas de cada día
        resultados_max = pool.starmap(buscar_maxima, argumentos)
        resultados_min = pool.starmap(buscar_minima, argumentos)


    print("Escribiendo resultados en ficheros finales...")
    
    # Guardamos las rutas de los ficheros 'maximas' y 'minimas'
    ruta_maximas = os.path.join(CARPETA, "maximas.txt")
    ruta_minimas = os.path.join(CARPETA, "minimas.txt")

    # Abrimos ambos archivos en modo escritura e insertamos sus datos respectivos
    with open(ruta_maximas, "w") as f:
        for dato in resultados_max:
            if dato: 
                f.write(dato)


    with open(ruta_minimas, "w") as f:
        for dato in resultados_min:
            if dato:
                f.write(dato)

    print("Proceso finalizado. Revisa la carpeta Ficheros.")