import threading
import time
import random

class WorkerThread(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        while True:
            print(f"Soy {self.name} y estoy trabajando")
            
            sleep_time = random.randint(1, 10)
            time.sleep(sleep_time)
            
            print(f"Soy {self.name} y he terminado de trabajar")