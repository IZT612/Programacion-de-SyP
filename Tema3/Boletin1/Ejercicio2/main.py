from classes import CounterThread

def main():
    hilos = []

    for i in range(10):
        hilo = CounterThread(f"Hilo-{i+1}")
        hilos.append(hilo)
        hilo.start()

    for h in hilos:
        h.join()

    print(f"Cuenta final: {CounterThread.cuenta}")

if __name__ == "__main__":
    main()