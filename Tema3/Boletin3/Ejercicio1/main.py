import time
import threading
from classes import Corredor

def main():
    hilos = [Corredor(i) for i in range(1, 11)]


    for h in hilos:
        h.start()

    print("Corredores a sus puestos...")
    time.sleep(1)
    
    for i in range(3, 0, -1):
        print(f"Juez: {i}...")
        time.sleep(1)

    print("¡YA!")

    Corredor.evento_salida.set()

    for h in hilos:
        h.join()

    print("La carrera ha terminado.")

if __name__ == "__main__":
    main()