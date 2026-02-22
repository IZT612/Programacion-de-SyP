import random
from classes import AdivinadorLock

def main():
    AdivinadorLock.numero_oculto = random.randint(0, 100)
    hilos = [AdivinadorLock(f"Hilo-{i}") for i in range(10)]
    
    for h in hilos: h.start()
    for h in hilos: h.join()
    
    print("Fin del juego.")

if __name__ == "__main__":
    main()