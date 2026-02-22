import threading
import time
import random

class ClienteCarniceria(threading.Thread):
    sem_carniceros = threading.Semaphore(4)

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        print(f"{self.name} entra a la carnicería.")
        
        with ClienteCarniceria.sem_carniceros:
            print(f"El {self.name} está siendo atendido.")
            time.sleep(random.randint(1, 10))
            print(f"El {self.name} ha terminado en la carnicería.")