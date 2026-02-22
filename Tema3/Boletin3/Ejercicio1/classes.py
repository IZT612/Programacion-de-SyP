import threading
import time
import random

class Corredor(threading.Thread):

    evento_salida = threading.Event()

    def __init__(self, dorsal):
        super().__init__()
        self.dorsal = dorsal

    def run(self):
        print(f"Corredor {self.dorsal} está en la línea de salida.")
        
        Corredor.evento_salida.wait()
        
        inicio = time.time()
        time.sleep(random.uniform(1, 3))
        fin = time.time()
        
        tiempo_total = fin - inicio
        print(f"🏁 Corredor {self.dorsal} llegó a la meta en {tiempo_total:.4f} segundos.")