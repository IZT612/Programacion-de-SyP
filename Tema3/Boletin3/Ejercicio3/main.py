import time
import random
from classes import Peaton, Semaforo

def main():
    controlador = Semaforo()
    controlador.start()

    peatones = []
    for i in range(10):
        p = Peaton(f"Peatón-{i}")
        peatones.append(p)
        p.start()
        time.sleep(random.uniform(0.5, 1))

    for p in peatones:
        p.join()
    
    controlador.join()
    print("Simulación terminada.")

if __name__ == "__main__":
    main()