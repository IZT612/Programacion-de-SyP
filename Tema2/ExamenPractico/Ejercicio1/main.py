import multiprocessing
import os
from functions import generar_temperaturas, buscar_maxima, buscar_minima, CARPETA

if __name__ == "__main__":
    
    mes = 12
    # Preparamos la lista de argumentos: [(1, 12), (2, 12), ..., (31, 12)]
    argumentos = [(dia, mes) for dia in range(1, 32)]

    print("--- FASE 1: Generación de ficheros con Pool ---")
    
    # Creamos un Pool. Python decide cuántos procesos usar (suele ser nº de núcleos CPU)
    with multiprocessing.Pool() as pool:
        # starmap ejecuta 'generar_temperaturas' para cada par de argumentos
        pool.starmap(generar_temperaturas, argumentos)
        
    print("Fase 1 completada.\n")

    print("--- FASE 2: Cálculo de Máximas y Mínimas ---")
    
    # Usamos el Pool para calcular y RECUPERAR los datos
    with multiprocessing.Pool() as pool:
        # Lanzamos los procesos y guardamos lo que nos devuelven en variables
        resultados_max = pool.starmap(buscar_maxima, argumentos)
        resultados_min = pool.starmap(buscar_minima, argumentos)

    # --- FASE 3: Escritura centralizada (Solo el Main escribe) ---
    print("Escribiendo resultados en ficheros finales...")
    
    ruta_maximas = os.path.join(CARPETA, "maximas.txt")
    ruta_minimas = os.path.join(CARPETA, "minimas.txt")

    # Escribimos Máximas
    with open(ruta_maximas, "w") as f:
        for dato in resultados_max:
            if dato: # Si no es None (por si algún fichero falló)
                f.write(dato)

    # Escribimos Mínimas
    with open(ruta_minimas, "w") as f:
        for dato in resultados_min:
            if dato:
                f.write(dato)

    print("Proceso finalizado. Revisa la carpeta Ficheros.")