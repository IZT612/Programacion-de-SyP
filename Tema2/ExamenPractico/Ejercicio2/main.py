import multiprocessing
from functions import (
    proceso1_leer_departamento, 
    proceso2_filtrar_salario, 
    proceso3_escribir_fichero
)

if __name__ == "__main__":
    print("--- GESTIÓN DE EMPLEADOS ---")
    
    # 1. Pedir datos al usuario
    # (Usa 'Desarrollo' o 'Finanzas' para probar, que tienen varios)
    dept_input = input("Introduce el departamento a filtrar: ")
    
    try:
        salario_input = int(input("Introduce el salario mínimo: "))
    except ValueError:
        print("El salario debe ser un número.")
        exit()

    # 2. Crear las vías de comunicación (Colas)
    # Cola 1: P1 -> P2
    cola_p1_p2 = multiprocessing.Queue()
    # Cola 2: P2 -> P3
    cola_p2_p3 = multiprocessing.Queue()

    # 3. Definir los procesos
    p1 = multiprocessing.Process(
        target=proceso1_leer_departamento, 
        args=(cola_p1_p2, dept_input)
    )
    
    p2 = multiprocessing.Process(
        target=proceso2_filtrar_salario, 
        args=(cola_p1_p2, cola_p2_p3, salario_input)
    )
    
    p3 = multiprocessing.Process(
        target=proceso3_escribir_fichero, 
        args=(cola_p2_p3,)
    )

    # 4. Lanzar procesos (El orden de start da igual, pero el lógico es 1,2,3)
    p1.start()
    p2.start()
    p3.start()

    # 5. Esperar a que terminen (Join)
    # El orden de join SÍ importa para cerrar limpio, esperamos en cascada.
    p1.join()
    p2.join()
    p3.join()

    print("\n--- Todos los procesos han finalizado ---")
    print("Verifica el fichero 'empleados.txt' en la carpeta Ficheros.")