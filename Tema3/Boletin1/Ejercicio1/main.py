from classes import WorkerThread

def main():
    nombres = ["Ana", "Carlos", "Beatriz", "David", "Elena"]
    lista_hilos = []

    for nombre in nombres:
        hilo = WorkerThread(nombre)
        lista_hilos.append(hilo)
        hilo.start()

if __name__ == "__main__":
    main()