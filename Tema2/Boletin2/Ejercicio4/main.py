import os
import multiprocessing

# Proceso 1: Filtra las películas por año y las envía al Proceso 2
def proceso_1(ruta_fichero, anio, queue):
    if not os.path.exists(ruta_fichero):
        print(f"El archivo {ruta_fichero} no existe.")
        return

    # Leer las películas del archivo
    with open(ruta_fichero, 'r') as archivo:
        for linea in archivo:
            pelicula, año_estreno = linea.strip().split(';')
            if int(año_estreno) == anio:
                queue.put((pelicula, año_estreno))  # Enviar película y año al Proceso 2
    queue.put(None)  # Señal para indicar que no hay más películas que enviar

# Proceso 2: Recibe películas y las guarda en un fichero con el nombre del año de estreno
def proceso_2(queue):
    peliculas = []
    while True:
        pelicula = queue.get()
        if pelicula is None:
            break
        peliculas.append(pelicula)
    
    if peliculas:
        anio = peliculas[0][1]  # Usamos el año de la primera película para nombrar el archivo
        nombre_fichero = f"peliculas{anio}.txt"
        
        # Guardar las películas en el fichero
        with open(nombre_fichero, 'w') as f:
            for pelicula, año in peliculas:
                f.write(f"{pelicula};{año}\n")
        print(f"Películas del año {anio} guardadas en {nombre_fichero}")

# Función principal (Main) que pide los datos al usuario y lanza los procesos
def main():
    # Obtener el año y la ruta del fichero del usuario
    anio = int(input("Introduce el año de estreno (menor al actual): "))
    if anio >= 2026:  # Año actual (puedes cambiarlo por la fecha actual si lo deseas)
        print("El año debe ser menor al actual.")
        return
    
    ruta_fichero = input("Introduce la ruta del fichero con las películas: ")

    # Crear la cola para la comunicación entre los procesos
    queue = multiprocessing.Queue()

    # Crear los procesos
    p1 = multiprocessing.Process(target=proceso_1, args=(ruta_fichero, anio, queue))
    p2 = multiprocessing.Process(target=proceso_2, args=(queue,))
    
    # Iniciar los procesos
    p1.start()
    p2.start()

    # Esperar a que terminen los procesos
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
