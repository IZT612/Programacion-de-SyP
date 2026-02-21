import threading
import random

class AdivinadorThread(threading.Thread):

    numero_oculto = 0
    encontrado = False
    lock = threading.Lock()

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        while True:
            with AdivinadorThread.lock:
                if AdivinadorThread.encontrado:
                    return
            
            mi_intento = random.randint(0, 100)
            print(f"{self.name}: Mi intento es {mi_intento}")
            
            if mi_intento == AdivinadorThread.numero_oculto:
                with AdivinadorThread.lock:
                    if not AdivinadorThread.encontrado:
                        AdivinadorThread.encontrado = True
                        print(f"¡{self.name} HA ACERTADO! El número era {mi_intento}")
                return