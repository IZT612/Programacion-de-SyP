import threading
import time

class Trabajador(threading.Thread):
    barrera_inicio = threading.Barrier(5)
    
    evento_hay_pedido = threading.Event()
    
    lock_pedido = threading.Lock()

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre
        self.daemon = True 

    def run(self):
        print(f"{self.name} ha fichado y espera a sus compañeros.")
        
        Trabajador.barrera_inicio.wait()
        
        print(f"{self.name} YA ESTÁ EN SU PUESTO.")
        
        while True:
            Trabajador.evento_hay_pedido.wait()
            
            pedido_cogido = False
            
            with Trabajador.lock_pedido:
                if Trabajador.evento_hay_pedido.is_set():
                    Trabajador.evento_hay_pedido.clear()
                    pedido_cogido = True
            
            if pedido_cogido:
                print(f"{self.name} está PREPARANDO el pedido...")
                time.sleep(2)
                print(f"{self.name} terminó el pedido.")
            else:
                pass