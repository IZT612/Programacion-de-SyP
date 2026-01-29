import random
import multiprocessing
import os

# Obtenemos el directorio actual donde está el script main.py
directorio_actual = os.path.dirname(__file__)

# Crear la carpeta 'alumnos' dentro del directorio actual si no existe
ruta_carpeta = os.path.join(directorio_actual, 'alumnos')
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

# Proceso 1: Genera 6 números aleatorios entre 1 y 10 con decimales, los guarda en un archivo dentro de la carpeta 'alumnos'
def generar_notas(nombre_fichero):
    notas = [round(random.uniform(1, 10), 2) for _ in range(6)]
    with open(nombre_fichero, 'w') as f:
        for nota in notas:
            f.write(f"{nota}\n")
    print(f"Notas generadas y guardadas en {nombre_fichero}")

# Proceso 2: Calcula la media de las notas y guarda el resultado en medias.txt dentro de la carpeta 'alumnos'
def calcular_media(nombre_fichero, nombre_alumno):
    with open(nombre_fichero, 'r') as f:
        notas = [float(linea.strip()) for linea in f]
    media = sum(notas) / len(notas)
    
    # Guardamos las medias en el archivo medias.txt dentro de la carpeta 'alumnos'
    with open(os.path.join(ruta_carpeta, 'medias.txt'), 'a') as f:
        f.write(f"{media} {nombre_alumno}\n")
    
    print(f"Media de {nombre_alumno} calculada y guardada.")

# Proceso 3: Lee medias.txt y encuentra la mayor media
def obtener_maxima_media():
    max_media = -1
    mejor_alumno = ""
    
    with open(os.path.join(ruta_carpeta, 'medias.txt'), 'r') as f:
        for linea in f:
            media, alumno = linea.strip().split()
            media = float(media)
            if media > max_media:
                max_media = media
                mejor_alumno = alumno
    
    print(f"La mayor media es {max_media} y el alumno que la obtuvo es {mejor_alumno}")

# Función principal (Main) que lanza los procesos
def main():
    # Crear ficheros de notas
    procesos_generacion = []
    for i in range(1, 11):
        nombre_fichero = os.path.join(ruta_carpeta, f"Alumno{i}.txt")  # Guardamos en la carpeta 'alumnos'
        p1 = multiprocessing.Process(target=generar_notas, args=(nombre_fichero,))
        procesos_generacion.append(p1)
        p1.start()

    # Esperar que terminen los procesos de generación de notas
    for p in procesos_generacion:
        p.join()

    # Crear ficheros de medias
    procesos_media = []
    for i in range(1, 11):
        nombre_fichero = os.path.join(ruta_carpeta, f"Alumno{i}.txt")  # Ruta actualizada
        nombre_alumno = f"Alumno{i}"
        p2 = multiprocessing.Process(target=calcular_media, args=(nombre_fichero, nombre_alumno))
        procesos_media.append(p2)
        p2.start()

    # Esperar que terminen los procesos de cálculo de medias
    for p in procesos_media:
        p.join()

    # Obtener la máxima media
    p3 = multiprocessing.Process(target=obtener_maxima_media)
    p3.start()
    p3.join()

if __name__ == "__main__":
    main()
