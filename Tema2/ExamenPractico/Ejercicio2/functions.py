import os
import time

# Guardamos todas las rutas que vamos a utilizar
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA = os.path.join(DIRECTORIO_BASE, "Ficheros")
RUTA_SALARIOS = os.path.join(CARPETA, "salarios.txt")
RUTA_EMPLEADOS = os.path.join(CARPETA, "empleados.txt")

"""
Proceso 1

Se encarga de añadir en la cola todos los datos de cada empleado (excepto el departamento) que coincidan con el departamento 

Args:
    cola (Queue): Cola en la que insertaremos los datos encontrados
    departamento_buscado (String): Nombre del departamento que usaremos para filtrar
"""
def leer_departamento(cola, departamento_buscado):
    print(f"[P1] Iniciando búsqueda del departamento: {departamento_buscado}")
    
    try:
        with open(RUTA_SALARIOS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea: continue
                
                datos = linea.split(";")
                nombre = datos[0]
                apellido = datos[1]
                salario = int(datos[2])
                departamento = datos[3]

                if departamento.lower() == departamento_buscado.lower():

                    paquete = [nombre, apellido, salario]
                    cola.put(paquete)
                    
    except FileNotFoundError:
        print(f"[P1] Error: No se encuentra el fichero {RUTA_SALARIOS}")

    cola.put(None)
    print("[P1] Terminado.")

"""
Proceso 2

Se encarga de añadir en la cola los datos de aquellos empleados (post filtrado del proceso 1) cuyo salario esté por encima del recibido por parámetro

Args:
    cola_entrada (Queue): Cola desde la que recibirá los datos del proceso 1 (Datos de cada empleado filtrado según el departamento)
    cola_salida (Queue): Cola desde la que enviará los datos de toda persona tras su filtrado
    salario_minimo (int): Salario mínimo que se usará para filtrar
"""
def filtrar_salario(cola_entrada, cola_salida, salario_minimo):
    print(f"[P2] Filtrando salarios mayores a: {salario_minimo}")
    
    while True:
        datos = cola_entrada.get()

        if datos is None:
            cola_salida.put(None)
            break
        
        salario_actual = datos[2]
        
        if salario_actual >= salario_minimo:
            cola_salida.put(datos)

    print("[P2] Terminado.")

"""
Proceso 3

Se encarga de escribir todos los datos ya filtrados en un fichero 'empleados'

Args:
    cola_entrada (Queue): Cola desde la que recibirá los datos del proceso 2
"""
def escribir_fichero(cola_entrada):
    print("[P3] Iniciando escritura de fichero...")
    
    with open(RUTA_EMPLEADOS, "w", encoding="utf-8") as f:
        
        while True:
            datos = cola_entrada.get()
            
            if datos is None:
                break
            
            nombre = datos[0]
            apellido = datos[1]
            salario = datos[2]
            
            linea_a_escribir = f"{apellido} {nombre}, {salario}\n"
            f.write(linea_a_escribir)
            print(f"[P3] Escribiendo: {linea_a_escribir.strip()}")

    print(f"[P3] Terminado. Fichero generado en {RUTA_EMPLEADOS}")