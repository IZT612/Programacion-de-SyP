import multiprocessing
from functions import (
    leer_departamento, 
    filtrar_salario, 
    escribir_fichero
)

if __name__ == "__main__":
    print("--- GESTIÓN DE EMPLEADOS ---")
    
    # Pedimos el departamento para filtrar
    dept_input = input("Introduce el departamento a filtrar: ")
    
    # Pedimos el salario mínimo que deben tener los empleados
    try:
        salario_input = int(input("Introduce el salario mínimo: "))
    except ValueError:
        print("El salario debe ser un número.")
        exit()

    # Creamos dos colas, una para cada par de procesos (Similar a una pipe)
    cola_p1_p2 = multiprocessing.Queue()
    cola_p2_p3 = multiprocessing.Queue()

    # Definimos todos los procesos, indicando las funciones que usarán y los argumentos
    p1 = multiprocessing.Process(
        target=leer_departamento, 
        args=(cola_p1_p2, dept_input)
    )
    
    p2 = multiprocessing.Process(
        target=filtrar_salario, 
        args=(cola_p1_p2, cola_p2_p3, salario_input)
    )
    
    p3 = multiprocessing.Process(
        target=escribir_fichero, 
        args=(cola_p2_p3,)
    )

    # Iniciamos todos los procesos a la vez
    p1.start()
    p2.start()
    p3.start()

    # Una vez todos acaben, finalizamos el programa
    p1.join()
    p2.join()
    p3.join()

    print("\n--- Todos los procesos han finalizado ---")
    print("Verifica el fichero 'empleados.txt' en la carpeta Ficheros.")