import time
from classes import Trabajador

def main():
    trabajadores = [Trabajador(f"Trabajador-{i}") for i in range(5)]
    
    for t in trabajadores:
        t.start()

    time.sleep(2)
    print("\n--- ¡COMIENZA EL TURNO! ---\n")

    for i in range(3):
        print(f"\n🔔 JEFE: ¡NUEVO PEDIDO {i+1} DISPONIBLE!")
        Trabajador.evento_hay_pedido.set()
        
        time.sleep(4)

    print("\nFin del turno. Cerrando almacén.")

if __name__ == "__main__":
    main()