import threading
import time
import random

class Estudiante(threading.Thread):

    libros = [threading.Lock() for _ in range(9)]

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):

        libro1, libro2 = random.sample(range(9), 2)
        
        primero, segundo = sorted([libro1, libro2])

        print(f"{self.name} quiere los libros {primero} y {segundo}.")

        with Estudiante.libros[primero]:
            with Estudiante.libros[segundo]:
                print(f"📖 {self.name} está usando libros {primero} y {segundo}.")
                time.sleep(random.randint(3, 5))
                print(f"⬇️ {self.name} devuelve libros {primero} y {segundo}.")