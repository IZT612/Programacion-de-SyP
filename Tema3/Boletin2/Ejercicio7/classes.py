import threading
import time
import random
import queue


cola = queue.Queue(maxsize=1)

class Productor(threading.Thread):
    def run(self):
        for i in range(5):
            item = f"Producto-{i}"
            print(f"Productor intentando poner {item}...")
            cola.put(item) 
            print(f"✅ Productor puso {item}")
            time.sleep(random.uniform(0.5, 1))

class Consumidor(threading.Thread):
    def run(self):
        for i in range(5):
            print("Consumidor esperando...")
            item = cola.get() 
            print(f"😋 Consumidor obtuvo {item}")
            cola.task_done()
            time.sleep(random.uniform(1, 2))