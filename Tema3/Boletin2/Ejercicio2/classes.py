import threading
import time
import random

class ClientePanaderia(threading.Thread):
    dependiente = threading.Lock()

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        print(f"{self.name} está esperando en la cola.")
        
        with ClientePanaderia.dependiente:
            print(f"--- {self.name} está siendo atendido ---")
            time.sleep(random.randint(1, 5))
            print(f"--- {self.name} ha terminado de ser atendido ---")