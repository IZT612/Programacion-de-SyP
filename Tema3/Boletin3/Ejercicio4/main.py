import time
from classes import Trabajador

def main():
    trabajadores = [Trabajador(f"Trabajador-{i}") for i in range(5)]
    
    for t in trabajadores:
        t.start()

    time.sleep(1) 
    print("\n--- TODOS LOS TRABAJADORES ESTÁN LISTOS, EL TURNO COMIENZA ---\n")

    for i in range(3):
        print(f"\nJEFE: ¡NUEVO PEDIDO {i+1} DISPONIBLE!")
        Trabajador.evento_hay_pedido.set()
        
        time.sleep(3)

    print("\nFin del turno. Cerrando almacén.")

if __name__ == "__main__":
    main()