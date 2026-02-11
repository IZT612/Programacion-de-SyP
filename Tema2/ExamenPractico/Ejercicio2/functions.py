import os
import time

# --- CONFIGURACIÓN DE RUTAS ---
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA = os.path.join(DIRECTORIO_BASE, "Ficheros")
RUTA_SALARIOS = os.path.join(CARPETA, "salarios.txt")
RUTA_EMPLEADOS = os.path.join(CARPETA, "empleados.txt")

# --- PROCESO 1: Filtrar por Departamento ---
def proceso1_leer_departamento(cola_salida, departamento_buscado):
    print(f"[P1] Iniciando búsqueda del departamento: {departamento_buscado}")
    
    try:
        with open(RUTA_SALARIOS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea: continue
                
                # Desglosamos: María;Gómez;2500;Recursos Humanos
                datos = linea.split(";")
                nombre = datos[0]
                apellido = datos[1]
                salario = int(datos[2])
                departamento = datos[3]

                # Si coincide el departamento
                if departamento.lower() == departamento_buscado.lower():
                    # Enviamos todo MENOS el departamento (según enunciado)
                    paquete = [nombre, apellido, salario]
                    cola_salida.put(paquete)
                    
    except FileNotFoundError:
        print(f"[P1] Error: No se encuentra el fichero {RUTA_SALARIOS}")

    # SEÑAL DE FIN: Enviamos None para avisar al siguiente proceso que hemos terminado
    cola_salida.put(None)
    print("[P1] Terminado.")

# --- PROCESO 2: Filtrar por Salario ---
def proceso2_filtrar_salario(cola_entrada, cola_salida, salario_minimo):
    print(f"[P2] Filtrando salarios mayores a: {salario_minimo}")
    
    while True:
        # 1. Esperamos recibir datos del Proceso 1
        datos = cola_entrada.get()

        # 2. Si recibimos None, es que P1 ha terminado. Nosotros también terminamos.
        if datos is None:
            cola_salida.put(None) # Avisamos a P3
            break
        
        # 3. Procesamos los datos: [Nombre, Apellido, Salario]
        salario_actual = datos[2]
        
        if salario_actual >= salario_minimo:
            # Enviamos tal cual nos llega al siguiente proceso
            cola_salida.put(datos)

    print("[P2] Terminado.")

# --- PROCESO 3: Escribir Fichero Final ---
def proceso3_escribir_fichero(cola_entrada):
    print("[P3] Iniciando escritura de fichero...")
    
    # Abrimos el fichero en modo escritura ("w")
    # Es seguro hacerlo aquí porque SOLO este proceso escribe en él.
    with open(RUTA_EMPLEADOS, "w", encoding="utf-8") as f:
        
        while True:
            # 1. Recibimos datos del Proceso 2
            datos = cola_entrada.get()
            
            # 2. Si es None, P2 ha terminado. Nosotros cerramos el chiringuito.
            if datos is None:
                break
            
            # 3. Formateamos: Apellido Nombre, Salario
            nombre = datos[0]
            apellido = datos[1]
            salario = datos[2]
            
            linea_a_escribir = f"{apellido} {nombre}, {salario}\n"
            f.write(linea_a_escribir)
            print(f"[P3] Escribiendo: {linea_a_escribir.strip()}")

    print(f"[P3] Terminado. Fichero generado en {RUTA_EMPLEADOS}")