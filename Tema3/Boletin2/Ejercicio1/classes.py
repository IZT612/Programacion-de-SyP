import threading
import random
import time

class AdivinadorLock(threading.Thread):
    numero_oculto = 0
    encontrado = False
    lock = threading.Lock()

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        while True:
            mi_intento = random.randint(0, 100)
            
            with AdivinadorLock.lock:
                if AdivinadorLock.encontrado:
                    return 
                
                print(f"{self.name}: Mi intento: {mi_intento}")
                if mi_intento == AdivinadorLock.numero_oculto:
                    AdivinadorLock.encontrado = True
                    print(f"¡{self.name} ACERTÓ! El número era {mi_intento}")
                    return
                else:
                    pass
            
            # Pausa por que si no este hilo no deja el paso a los demas
            time.sleep(0.1)