import threading
import time
import random

class ClienteCompleto(threading.Thread):
    sem_carniceria = threading.Semaphore(4)
    sem_charcuteria = threading.Semaphore(2)

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre
        self.pasado_carniceria = False
        self.pasado_charcuteria = False

    def run(self):
        while not (self.pasado_carniceria and self.pasado_charcuteria):
            if not self.pasado_carniceria:

                if ClienteCompleto.sem_carniceria.acquire(blocking=False):
                    try:
                        print(f"{self.name} atendido en CARNICERÍA.")
                        time.sleep(random.uniform(0.5, 2))
                        self.pasado_carniceria = True
                    finally:
                        ClienteCompleto.sem_carniceria.release()
                    continue

            if not self.pasado_charcuteria:
                if ClienteCompleto.sem_charcuteria.acquire(blocking=False):
                    try:
                        print(f"{self.name} atendido en CHARCUTERÍA.")
                        time.sleep(random.uniform(0.5, 2))
                        self.pasado_charcuteria = True
                    finally:
                        ClienteCompleto.sem_charcuteria.release()
                    continue

            time.sleep(0.5)

        print(f"{self.name} ha terminado TODO.")