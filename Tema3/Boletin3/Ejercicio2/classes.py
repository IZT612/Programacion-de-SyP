import threading
import random
import time

class JugadorEscape(threading.Thread):
    clave_correcta = 0
    
    evento_encontrado = threading.Event()
    
    barrera_salida = threading.Barrier(5)

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        while not JugadorEscape.evento_encontrado.is_set():
            intento = random.randint(0, 5000)
            
            if intento == JugadorEscape.clave_correcta:
                print(f"¡{self.name} ENCONTRÓ LA CLAVE ({intento})!")
                JugadorEscape.evento_encontrado.set()
            
            time.sleep(0.01)

        print(f"{self.name} va a la puerta esperando al grupo...")
        
        try:
            JugadorEscape.barrera_salida.wait()
        except threading.BrokenBarrierError:
            pass

        print(f"{self.name} ha salido de la habitación.")