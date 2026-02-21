import random
from classes import AdivinadorThread

def main():
    AdivinadorThread.numero_oculto = random.randint(0, 100)
    print(f"--- El número secreto (para debug) es: {AdivinadorThread.numero_oculto} ---")

    hilos = []
    
    for i in range(10):
        t = AdivinadorThread(f"Buscador-{i+1}")
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    print("Juego terminado.")

if __name__ == "__main__":
    main()