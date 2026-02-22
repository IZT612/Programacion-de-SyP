import threading
import time
import random

class Filosofo(threading.Thread):
    palillos = [threading.Lock() for _ in range(5)]

    def __init__(self, id_filosofo):
        super().__init__()
        self.id = id_filosofo
        self.name = f"Filósofo {id_filosofo}"
        self.palillo_izq = id_filosofo
        self.palillo_der = (id_filosofo + 1) % 5

    def run(self):
        print(f"{self.name} está pensando...")
        time.sleep(random.uniform(1, 2))

        primero = min(self.palillo_izq, self.palillo_der)
        segundo = max(self.palillo_izq, self.palillo_der)

        with Filosofo.palillos[primero]:
            with Filosofo.palillos[segundo]:
                print(f"{self.name} está COMIENDO.")
                time.sleep(random.uniform(1, 2))
                print(f"{self.name} terminó de comer.")