import threading
import time
import random

evento_semaforo = threading.Event()

class Peaton(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        print(f"{self.name} llega al paso de peatones y espera.")
        
        evento_semaforo.wait()
        
        print(f"{self.name} cruza la calle.")
        time.sleep(0.5)

class Semaforo(threading.Thread):
    def run(self):
        for _ in range(3): 
            print("\nSEMÁFORO EN ROJO (Peatones esperan)...")
            evento_semaforo.clear()
            time.sleep(3)
            
            print("\nSEMÁFORO EN VERDE (Pueden cruzar)...")
            evento_semaforo.set()
            time.sleep(2)
        
        evento_semaforo.set()