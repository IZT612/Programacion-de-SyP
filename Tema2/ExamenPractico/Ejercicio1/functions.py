import random
import os

# Definimos el nombre de la carpeta
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA = os.path.join(DIRECTORIO_BASE, "Ficheros")

ruta_maximas = os.path.join(CARPETA, "maximas.txt")
ruta_minimas = os.path.join(CARPETA, "minimas.txt")

def preparar_ficheros_resultados():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

    ruta_maximas = os.path.join(CARPETA, "maximas.txt")
    ruta_minimas = os.path.join(CARPETA, "minimas.txt")

    with open(ruta_maximas, "w") as f:
        pass 
    
    with open(ruta_minimas, "w") as f:
        pass

# --- PROCESO 1: Generar Temperaturas ---
def generar_temperaturas(dia, mes):
    # Creamos el nombre: "01-12.txt"
    nombre_archivo = f"{dia:02d}-{mes:02d}.txt"
    # Unimos la carpeta con el nombre: "Ficheros/01-12.txt"
    ruta_completa = os.path.join(CARPETA, nombre_archivo)

    try:
        # El modo "w" sobrescribe el fichero si ya existe (lo vacía y escribe de nuevo)
        with open(ruta_completa, "w") as f:
            for _ in range(24):
                # Aleatorio entre 0 y 20 con 2 decimales
                temp = round(random.uniform(0, 20), 2)
                f.write(f"{temp}\n")
    except Exception as e:
        print(f"Error generando fichero {ruta_completa}: {e}")

# --- PROCESO 2: Buscar Máximas ---
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

# --- PROCESO 3: Buscar Mínimas ---
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
            # --- CAMBIO IMPORTANTE ---
            # Devolvemos el texto al Main.
            return f"{etiqueta}:{minima}\n"

    except FileNotFoundError:
        return None