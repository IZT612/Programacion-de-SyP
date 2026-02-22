import threading
import random
import time

class AdivinadorThread(threading.Thread):
    # Variable compartida SIN Lock
    numero_oculto = 0
    encontrado = False

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        while True:
            if AdivinadorThread.encontrado:
                return

            mi_intento = random.randint(0, 100)
            
            print(f"{self.name}: Mi intento es {mi_intento}")

            if mi_intento == AdivinadorThread.numero_oculto:
                if not AdivinadorThread.encontrado:
                    AdivinadorThread.encontrado = True
                    print(f"¡{self.name} HA ACERTADO! El número era {mi_intento}")
                return
            
            time.sleep(random.uniform(0.1, 0.5))