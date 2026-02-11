import random
import os

# Guardamos la ruta de la carpeta donde guardaremos los ficheros
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA = os.path.join(DIRECTORIO_BASE, "Ficheros")

# Rutas de los ficheros de temperatura maxima y minima
ruta_maximas = os.path.join(CARPETA, "maximas.txt")
ruta_minimas = os.path.join(CARPETA, "minimas.txt")


"""
Proceso 1

Genera el nombre del archivo según el día y mes recibidos mediante parámetros, genera 24 temperaturas aleatorias y las escribe en el fichero

Args:
    dia (int): Día en el que se midieron las temperaturas.
    mes (int): Mes en el que se midieron las temperaturas.
"""
def generar_temperaturas(dia, mes):

    nombre_archivo = f"{dia:02d}-{mes:02d}.txt"

    ruta_completa = os.path.join(CARPETA, nombre_archivo)

    try:

        with open(ruta_completa, "w") as f:
            for _ in range(24):

                temp = round(random.uniform(0, 20), 2)
                f.write(f"{temp}\n")
    except Exception as e:
        print(f"Error generando fichero {ruta_completa}: {e}")

"""
Proceso 2

Busca en un fichero que coincida con el día y mes recibidos por parametros la temperatura máxima registrada

Args:
    dia (int): Día del fichero en el que buscar la temp máxima
    mes (int): Mes del fichero en el que buscar la temp máxima

Return: String que escribir en el fichero 'maximas.txt' con el siguiente formato: 'dia-mes:temperatura'
"""
def buscar_maxima(dia, mes):    
    etiqueta = f"{dia:02d}-{mes:02d}"
    nombre_fichero = f"{etiqueta}.txt"
    ruta_lectura = os.path.join(CARPETA, nombre_fichero)
    
    try:
        temps = []
        with open(ruta_lectura, "r") as f:
            for linea in f:
                temps.append(float(linea.strip()))
        
        if temps:
            maxima = max(temps)

            return f"{etiqueta}:{maxima}\n"
            
    except FileNotFoundError:
        return None

"""
Proceso 3

Busca en un fichero que coincida con el día y mes recibidos por parametros la temperatura mínima registrada

Args:
    dia (int): Día del fichero en el que buscar la temp mínima
    mes (int): Mes del fichero en el que buscar la temp mínima

Return: String que escribir en el fichero 'minimas.txt' con el siguiente formato: 'dia-mes:temperatura'
"""
def buscar_minima(dia, mes):
    etiqueta = f"{dia:02d}-{mes:02d}"
    nombre_fichero = f"{etiqueta}.txt"
    ruta_lectura = os.path.join(CARPETA, nombre_fichero)
    
    try:
        temps = []
        with open(ruta_lectura, "r") as f:
            for linea in f:
                temps.append(float(linea.strip()))
        
        if temps:
            minima = min(temps)
            return f"{etiqueta}:{minima}\n"

    except FileNotFoundError:
        return None